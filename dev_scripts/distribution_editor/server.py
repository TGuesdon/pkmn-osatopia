#!/usr/bin/env python3
"""Éditeur de répartition des Pokémon : rencontres sauvages et équipes des dresseurs.

Lit et réécrit directement :
  - src/data/wild_encounters.json
  - src/data/trainers.party

Usage : python3 dev_scripts/distribution_editor/server.py [port]
"""
import hashlib
import io
import json
import re
import sys
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
WILD_PATH = ROOT / 'src/data/wild_encounters.json'
PARTY_PATH = ROOT / 'src/data/trainers.party'
CUSTOM_MARKER = 'You may add any custom species below this point'


def read(rel):
    return (ROOT / rel).read_text(encoding='utf-8')


def sha(text):
    return hashlib.sha1(text.encode('utf-8')).hexdigest()


def strip_comments(s):
    return re.sub(r'//[^\n]*', '', re.sub(r'/\*[\s\S]*?\*/', '', s))


def humanize(const, prefix):
    """SPECIES_MR_MIME -> 'Mr Mime' : reconverti à l'identique par trainerproc."""
    return ' '.join(w.capitalize() for w in const[len(prefix):].split('_'))


# ---------- Conversions de trainerproc (tools/trainerproc/main.c) ----------

def to_constant(text, prefix):
    """Port de fprint_constant : 'Oran Berry' -> ITEM_ORAN_BERRY."""
    text = text.strip()
    out = '' if text.startswith(prefix + '_') else prefix + '_'
    if not text:
        return out + 'NONE'
    for c in text:
        if c.isascii() and c.isalnum():
            out += c.upper()
        elif c == "'":
            pass
        else:
            out += '_'
    return out


def to_species(text):
    """Port de fprint_species : 'Nidoran♀' -> SPECIES_NIDORAN_F."""
    text = text.strip()
    out = '' if text.startswith('SPECIES_') else 'SPECIES_'
    if not text:
        return out + 'NONE'
    underscore = False
    for c in text:
        if c.isascii() and c.isalnum():
            if underscore:
                out += '_'
            underscore = False
            out += c.upper()
        elif c in "'%’":
            pass
        elif c == '♂':
            underscore = False
            out += '_M'
        elif c == '♀':
            underscore = False
            out += '_F'
        elif c == 'é':
            if underscore:
                out += '_'
            underscore = False
            out += 'E'
        else:
            underscore = True
    return out


# ---------- Espèces ----------

def gfx_paths(text, prefix):
    out = {}
    for m in re.finditer(r'(' + prefix + r'\w+)\[\]\s*=\s*INCBIN_U\d+\("([^"]+)"\)', text):
        out.setdefault(m.group(1), re.sub(r'\.(4bpp|8bpp)(\.\w+)?$', '.png', m.group(2)))
    return out


def parse_species_blocks(text):
    heads = list(re.finditer(r'^\s*\[(SPECIES_\w+)\]\s*=', text, re.M))
    for i, h in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        yield h.group(1), text[h.end():end]


def first_num(raw):
    if raw is None:
        return None
    t = re.search(r'\?\s*(-?\d+)\s*:', raw)
    if t:
        return int(t.group(1))
    m = re.search(r'-?\d+', raw)
    return int(m.group(0)) if m else None


def load_species():
    consts, aliases = [], set()
    for m in re.finditer(r'^#define (SPECIES_\w+)\s+(.+)$', read('include/constants/species.h'), re.M):
        name, val = m.group(1), m.group(2).strip()
        if re.fullmatch(r'SPECIES_\w+', val):
            aliases.add(name)  # ex. SPECIES_CASTFORM -> SPECIES_CASTFORM_NORMAL, accepté par trainerproc
            continue
        if name in ('SPECIES_NONE', 'SPECIES_EGG'):
            continue
        if not re.match(r'^\d+$', val):
            continue
        consts.append(name)

    gfx = gfx_paths(read('src/data/graphics/pokemon.h'), 'gMon')
    info = read('src/data/pokemon/species_info.h')
    marker = info.find(CUSTOM_MARKER)
    custom_text = strip_comments(info[marker:]) if marker >= 0 else ''
    sources = [(strip_comments(p.read_text(encoding='utf-8')), False)
               for p in sorted((ROOT / 'src/data/pokemon/species_info').glob('gen_*_families.h'))]
    sources.append((custom_text, True))

    hoenn = {}
    m = re.search(r'enum HoennDexOrder\s*\{([\s\S]*?)\}', read('include/constants/pokedex.h'))
    if m:
        for i, x in enumerate(re.findall(r'HOENN_DEX_(\w+)', m.group(1))):
            hoenn.setdefault('SPECIES_' + x, i)

    species = {}
    for text, custom in sources:
        for sid, body in parse_species_blocks(text):
            if sid in species and not custom:
                continue
            name = re.search(r'\.speciesName\s*=\s*_\("([^"]*)"\)', body)
            front = re.search(r'\.frontPic\s*=\s*(gMon\w+)', body)
            types = re.search(r'\.types\s*=\s*MON_TYPES\(([^)]*)\)', body)
            stats = [first_num((re.search(r'\.' + k + r'\s*=\s*([^,\n]+)', body) or [None, None])[1])
                     for k in ('baseHP', 'baseAttack', 'baseDefense', 'baseSpAttack', 'baseSpDefense', 'baseSpeed')]
            evos = [{'method': e[0].replace('EVO_', ''), 'param': e[1].strip(), 'target': e[2]}
                    for e in re.findall(r'\{\s*(EVO_\w+)\s*,\s*([^,]+?)\s*,\s*(SPECIES_\w+)', body)
                    if e[2] != 'SPECIES_NONE']
            species[sid] = {
                'id': sid,
                'name': name.group(1) if name else humanize(sid, 'SPECIES_'),
                'types': list(dict.fromkeys(t.strip().replace('TYPE_', '') for t in types.group(1).split(','))) if types else [],
                'front': gfx.get(front.group(1)) if front else None,
                'custom': custom,
                'bst': sum(s or 0 for s in stats),
                'evos': evos,
                'dex': hoenn.get(sid),
            }
    out = []
    for c in consts:
        s = species.get(c)
        if s and not s['front']:
            guess = f"graphics/pokemon/{s['name'].lower()}/anim_front.png"
            s['front'] = guess if (ROOT / guess).is_file() else None
        s = s or {'id': c, 'name': humanize(c, 'SPECIES_'), 'types': [], 'front': None,
                               'custom': False, 'bst': 0, 'evos': [], 'dex': None}
        out.append(s)
    # Pré-évolutions, pour afficher la chaîne dans le sélecteur.
    by_id = {s['id']: s for s in out}
    for s in out:
        for e in s['evos']:
            if e['target'] in by_id:
                by_id[e['target']].setdefault('from', []).append({'id': s['id'], 'method': e['method'], 'param': e['param']})
    return out, aliases


# ---------- Maps ----------

def load_maps():
    sections = {s['id']: s for s in json.loads(read('src/data/region_map/region_map_sections.json'))['map_sections']}
    rematch = {}
    for m in re.finditer(r'REMATCH\(([^)]*)\)', read('src/battle_setup.c')):
        parts = [p.strip() for p in m.group(1).split(',')]
        if parts and parts[-1].startswith('MAP_'):
            rematch.setdefault(parts[-1], []).extend(p for p in parts[:-1] if p.startswith('TRAINER_') and p != 'TRAINER_NONE')
    maps = []
    for d in sorted((ROOT / 'data/maps').iterdir()):
        mj = d / 'map.json'
        if not mj.is_file():
            continue
        j = json.loads(mj.read_text(encoding='utf-8'))
        trainers = []
        scripts = d / 'scripts.inc'
        if scripts.is_file():
            for line in scripts.read_text(encoding='utf-8').splitlines():
                if 'trainerbattle' in line:
                    trainers += [t for t in re.findall(r'\b(TRAINER_[A-Z0-9_]+)\b', line) if not t.startswith('TRAINER_BATTLE_')]
        trainers += rematch.get(j['id'], [])
        sec = sections.get(j.get('region_map_section'), {})
        maps.append({
            'id': j['id'],
            'folder': d.name,
            'name': re.sub(r'(?<=[a-z])(?=[A-Z0-9])|_', ' ', d.name).replace('  ', ' '),
            'mapsec': j.get('region_map_section'),
            'mapsecName': sec.get('name', '').title(),
            'type': j.get('map_type', ''),
            'trainers': list(dict.fromkeys(trainers)),
        })
    return maps, list(sections.values())


# ---------- trainers.party ----------

def parse_mon(lines):
    head = lines[0]
    item = None
    if '@' in head:
        head, item = head.split('@', 1)
        item = item.strip()
    head = head.strip()
    gender = None
    m = re.search(r'\s*\((M|F)\)$', head)
    if m:
        gender = m.group(1)
        head = head[:m.start()].strip()
    nickname = None
    m = re.fullmatch(r'(.*\S)\s*\(([^()]+)\)', head)
    if m:
        nickname, head = m.group(1), m.group(2).strip()
    mon = {'speciesText': head, 'species': to_species(head), 'nickname': nickname, 'gender': gender,
           'item': item, 'level': None, 'levelIdx': None, 'attrs': [], 'moves': []}
    for line in lines[1:]:
        if line.startswith('- '):
            mon['moves'].append(line[2:].strip())
        elif re.match(r'^Level\s*:', line):
            mon['levelIdx'] = len(mon['attrs'])
            mon['level'] = first_num(line.split(':', 1)[1])
        else:
            mon['attrs'].append(line)
    return mon


def serialize_mon(mon):
    species = mon['species']
    text = mon.get('speciesText') if mon.get('speciesText') and to_species(mon['speciesText']) == species else humanize(species, 'SPECIES_')
    head = f"{mon['nickname']} ({text})" if mon.get('nickname') else text
    if mon.get('gender') in ('M', 'F'):
        head += f" ({mon['gender']})"
    if mon.get('item'):
        head += f" @ {mon['item'].strip()}"
    attrs = list(mon.get('attrs') or [])
    if mon.get('level') is not None:
        idx = mon.get('levelIdx')
        attrs.insert(idx if idx is not None and idx <= len(attrs) else 0, f"Level: {int(mon['level'])}")
    return [head] + attrs + [f'- {m.strip()}' for m in mon.get('moves') or [] if m.strip()]


def split_party_file(text):
    """Découpe trainers.party en blocs : (id, ligne_début, ligne_fin_header, ligne_fin)."""
    lines = text.split('\n')
    starts = [i for i, l in enumerate(lines) if l.startswith('=== ')]
    blocks = []
    for n, s in enumerate(starts):
        e = starts[n + 1] if n + 1 < len(starts) else len(lines)
        h = s + 1
        while h < e and lines[h].strip():
            h += 1
        blocks.append((lines[s][4:].strip(' ='), s, h, e))
    return lines, blocks


def load_trainers(text, pics):
    lines, blocks = split_party_file(text)
    out = []
    for tid, s, h, e in blocks:
        header = {}
        for l in lines[s + 1:h]:
            if ':' in l:
                k, v = l.split(':', 1)
                header[k.strip()] = v.strip()
        body = lines[h:e]
        readonly = any('/*' in l or '*/' in l for l in lines[s:e]) or any(k in header for k in ('Party Size', 'Pool Rules', 'Pool Pick Functions', 'Pool Prune'))
        chunks, cur = [], []
        for l in body:
            if l.strip():
                cur.append(l.rstrip())
            elif cur:
                chunks.append(cur)
                cur = []
        if cur:
            chunks.append(cur)
        pic = header.get('Pic', '')
        out.append({
            'id': tid,
            'name': header.get('Name', ''),
            'cls': header.get('Class', ''),
            'pic': pics.get(to_constant(pic, 'TRAINER_PIC')) if pic else None,
            'double': header.get('Double Battle', '').lower() == 'yes' or header.get('Battle Type', '').lower() == 'doubles',
            'items': header.get('Items', ''),
            'readonly': readonly,
            'party': [parse_mon(c) for c in chunks],
        })
    return out


def trainer_pics():
    text = read('src/data/graphics/trainers.h')
    paths = gfx_paths(text, 'gTrainerFrontPic_')
    out = {}
    for m in re.finditer(r'TRAINER_SPRITE\((TRAINER_PIC_\w+),\s*(gTrainerFrontPic_\w+)', text):
        if m.group(2) in paths:
            out[m.group(1)] = paths[m.group(2)]
    return out


# ---------- wild_encounters.json ----------

def dump_json(obj, indent=0):
    """Même format que le fichier d'origine : indentation de 4, listes de scalaires sur une ligne."""
    pad, inner = ' ' * indent, ' ' * (indent + 4)
    if isinstance(obj, dict):
        if not obj:
            return '{}'
        items = [f'{inner}{json.dumps(k, ensure_ascii=False)}: {dump_json(v, indent + 4)}' for k, v in obj.items()]
        return '{\n' + ',\n'.join(items) + '\n' + pad + '}'
    if isinstance(obj, list):
        if not obj:
            return '[]'
        if all(not isinstance(x, (dict, list)) for x in obj):
            return '[' + ', '.join(json.dumps(x, ensure_ascii=False) for x in obj) + ']'
        return '[\n' + ',\n'.join(inner + dump_json(x, indent + 4) for x in obj) + '\n' + pad + ']'
    return json.dumps(obj, ensure_ascii=False)


def wild_trailer(text):
    return text[len(text.rstrip()):]


# ---------- Validation ----------

def constants(rel, prefix):
    return set(re.findall(r'^#define (' + prefix + r'_\w+)\s', read(rel), re.M))


class Ctx:
    def __init__(self):
        self.lock = threading.Lock()
        self.species_ids = None
        self.moves = constants('include/constants/moves.h', 'MOVE')
        self.items = constants('include/constants/items.h', 'ITEM')


CTX = Ctx()


def build_data():
    species, aliases = load_species()
    CTX.species_ids = {s['id'] for s in species} | aliases
    maps, sections = load_maps()
    wild_text = WILD_PATH.read_text(encoding='utf-8')
    party_text = PARTY_PATH.read_text(encoding='utf-8')
    wild = json.loads(wild_text)
    group = next(g for g in wild['wild_encounter_groups'] if g.get('for_maps'))
    return {
        'species': species,
        'maps': maps,
        'sections': sections,
        'wildFields': group['fields'],
        'wild': group['encounters'],
        'trainers': load_trainers(party_text, trainer_pics()),
        'moves': sorted(humanize(m, 'MOVE_') for m in CTX.moves if m not in ('MOVE_NONE',) and not m.startswith('MOVE_UNAVAILABLE')),
        'items': sorted(humanize(i, 'ITEM_') for i in CTX.items if i != 'ITEM_NONE'),
        'versions': {'wild': sha(wild_text), 'party': sha(party_text)},
        'wildRoundTrip': dump_json(wild) + wild_trailer(wild_text) == wild_text,
    }


def validate_wild(encounters, fields):
    errors = []
    sizes = {f['type']: len(f['encounter_rates']) for f in fields}
    for enc in encounters:
        where = enc.get('map') or enc.get('base_label')
        for key, block in enc.items():
            if key not in sizes:
                continue
            mons = block.get('mons', [])
            if len(mons) != sizes[key]:
                errors.append(f'{where} / {key} : {len(mons)} emplacements au lieu de {sizes[key]}')
            for i, mon in enumerate(mons):
                if mon.get('species') not in CTX.species_ids:
                    errors.append(f'{where} / {key} #{i + 1} : espèce manquante ou inconnue ({mon.get("species")})')
                lo, hi = mon.get('min_level'), mon.get('max_level')
                if not (isinstance(lo, int) and isinstance(hi, int) and 1 <= lo <= hi <= 100):
                    errors.append(f'{where} / {key} #{i + 1} : niveaux invalides ({lo}-{hi})')
    return errors


def validate_party(tid, party):
    errors = []
    if not 1 <= len(party) <= 6:
        errors.append(f'{tid} : {len(party)} Pokémon (entre 1 et 6 attendus)')
    for i, mon in enumerate(party):
        w = f'{tid} #{i + 1}'
        if mon.get('species') not in CTX.species_ids:
            errors.append(f'{w} : espèce inconnue ({mon.get("species")})')
        lvl = mon.get('level')
        if lvl is not None and not (isinstance(lvl, int) and 1 <= lvl <= 100):
            errors.append(f'{w} : niveau invalide ({lvl})')
        if mon.get('item') and to_constant(mon['item'], 'ITEM') not in CTX.items:
            errors.append(f'{w} : objet inconnu « {mon["item"]} »')
        moves = [m for m in mon.get('moves') or [] if m.strip()]
        if len(moves) > 4:
            errors.append(f'{w} : plus de 4 attaques')
        for mv in moves:
            if to_constant(mv, 'MOVE') not in CTX.moves:
                errors.append(f'{w} : attaque inconnue « {mv} »')
    return errors


def save(payload):
    with CTX.lock:
        wild_text = WILD_PATH.read_text(encoding='utf-8')
        party_text = PARTY_PATH.read_text(encoding='utf-8')
        versions = payload.get('versions', {})
        if versions.get('wild') != sha(wild_text) or versions.get('party') != sha(party_text):
            return 409, {'errors': ['Les fichiers ont été modifiés sur le disque depuis le chargement. Recharge la page (tes modifications non enregistrées seront perdues).']}
        if CTX.species_ids is None:
            build_data()
        errors = []
        wild = json.loads(wild_text)
        group = next(g for g in wild['wild_encounter_groups'] if g.get('for_maps'))
        new_wild = payload.get('wild')
        if new_wild is not None:
            errors += validate_wild(new_wild, group['fields'])
        trainers = payload.get('trainers') or {}
        for tid, party in trainers.items():
            errors += validate_party(tid, party)
        lines, blocks = split_party_file(party_text)
        by_id = {b[0]: b for b in blocks}
        for tid in trainers:
            if tid not in by_id:
                errors.append(f'{tid} : dresseur introuvable dans trainers.party')
        if errors:
            return 400, {'errors': errors}

        if new_wild is not None:
            group['encounters'] = new_wild
            WILD_PATH.write_text(dump_json(wild) + wild_trailer(wild_text), encoding='utf-8')
        if trainers:
            # Remplace les sections d'équipe en partant de la fin pour garder les indices valides.
            for tid, s, h, e in sorted((by_id[t] for t in trainers), key=lambda b: -b[1]):
                body = []
                for mon in trainers[tid]:
                    body += serialize_mon(mon) + ['']
                lines[h + 1:e] = body
            PARTY_PATH.write_text('\n'.join(lines), encoding='utf-8')
        return 200, {'ok': True}


# ---------- Images ----------

_img_cache = {}


def sprite_png(rel):
    path = (ROOT / rel).resolve()
    if not str(path).startswith(str(ROOT / 'graphics') + '/') or path.suffix != '.png' or not path.is_file():
        return None
    if rel not in _img_cache:
        im = Image.open(path)
        if im.height == 2 * im.width:  # anim_front : deux frames empilées
            im = im.crop((0, 0, im.width, im.width))
        if im.mode == 'P':
            im.info['transparency'] = 0
            im = im.convert('RGBA')
        buf = io.BytesIO()
        im.save(buf, 'PNG')
        _img_cache[rel] = buf.getvalue()
    return _img_cache[rel]


def region_map_png():
    if 'region' not in _img_cache:
        ts = Image.open(ROOT / 'graphics/pokenav/region_map/map.png')
        data = (ROOT / 'graphics/pokenav/region_map/map.bin').read_bytes()
        tw = ts.width // 8
        out = Image.new('P', (240, 160))
        out.putpalette(ts.getpalette())
        for i, t in enumerate(data):
            x, y = (i % 64) * 8, (i // 64) * 8  # BG affine 64x64, une case = 1 octet
            if x < 240 and y < 160:
                out.paste(ts.crop(((t % tw) * 8, (t // tw) * 8, (t % tw) * 8 + 8, (t // tw) * 8 + 8)), (x, y))
        buf = io.BytesIO()
        out.convert('RGB').save(buf, 'PNG')
        _img_cache['region'] = buf.getvalue()
    return _img_cache['region']


# ---------- HTTP ----------

class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        if not self.path.startswith('/api/sprite'):
            sys.stderr.write('%s\n' % (fmt % args))

    def send(self, code, body, ctype):
        self.send_response(code)
        self.send_header('Content-Type', ctype)
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store' if ctype.startswith(('application/json', 'text/html')) else 'max-age=3600')
        self.end_headers()
        self.wfile.write(body)

    def send_json(self, code, obj):
        self.send(code, json.dumps(obj, ensure_ascii=False).encode('utf-8'), 'application/json; charset=utf-8')

    def do_GET(self):
        url = urlparse(self.path)
        try:
            if url.path in ('/', '/index.html'):
                self.send(200, (HERE / 'index.html').read_bytes(), 'text/html; charset=utf-8')
            elif url.path == '/api/data':
                with CTX.lock:
                    data = build_data()
                self.send_json(200, data)
            elif url.path == '/api/sprite':
                png = sprite_png(parse_qs(url.query).get('p', [''])[0])
                if png is None:
                    self.send(404, b'not found', 'text/plain')
                else:
                    self.send(200, png, 'image/png')
            elif url.path == '/api/region_map.png':
                self.send(200, region_map_png(), 'image/png')
            else:
                self.send(404, b'not found', 'text/plain')
        except Exception as e:  # noqa: BLE001 - outil local, on renvoie l'erreur telle quelle
            self.send_json(500, {'errors': [f'{type(e).__name__}: {e}']})

    def do_POST(self):
        if urlparse(self.path).path != '/api/save':
            return self.send(404, b'not found', 'text/plain')
        try:
            payload = json.loads(self.rfile.read(int(self.headers.get('Content-Length', 0))))
            code, body = save(payload)
            self.send_json(code, body)
        except Exception as e:  # noqa: BLE001
            self.send_json(500, {'errors': [f'{type(e).__name__}: {e}']})


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    port = int(args[0]) if args else 8643
    for p in range(port, port + 20):
        try:
            server = ThreadingHTTPServer(('127.0.0.1', p), Handler)
            break
        except OSError:
            continue
    else:
        sys.exit(f'Aucun port libre entre {port} et {port + 19}')
    url = f'http://localhost:{server.server_address[1]}/'
    print(f'Éditeur de répartition : {url}  (Ctrl+C pour arrêter)')
    if '--no-open' not in sys.argv:
        threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
