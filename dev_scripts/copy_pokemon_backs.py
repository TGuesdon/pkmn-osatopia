#!/usr/bin/env python3
"""
Copy back.png from each graphics/pokemon subfolder into a single backs/ folder
at the project root, renaming them as back0001.png, back0002.png, etc.
Upscales each image to 512x512 using ImageMagick with nearest-neighbour resampling.
Cleans the backs/ folder at the start of execution (removes all existing contents).
Writes a .txt file next to each PNG with a caption for the sprite.
Only copies the back.png at the root of each Pokémon folder (not from nested
subfolders like mega/).
"""

import shutil
import subprocess
from pathlib import Path
from typing import Tuple

TARGET_SIZE = (512, 512)
BACK_CAPTION = "pixback creature, back view, pixel art sprite"


def resize_nearest(path: Path, size: Tuple[int, int]) -> bool:
    """Resize image at path to size using ImageMagick nearest-neighbour (point) filter."""
    magick = shutil.which("magick") or shutil.which("convert")
    if not magick:
        return False
    w, h = size
    result = subprocess.run(
        [magick, str(path), "-filter", "point", "-resize", f"{w}x{h}!", str(path)],
        capture_output=True,
        text=True,
    )
    return result.returncode == 0


def main():
    # Resolve paths relative to project root (parent of dev_scripts)
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent
    pokemon_dir = project_root / "graphics" / "pokemon"
    backs_dir = project_root / "backs"

    if not pokemon_dir.is_dir():
        print(f"Error: {pokemon_dir} does not exist.")
        return 1

    # Clean backs folder: remove and recreate so it is empty
    if backs_dir.is_dir():
        shutil.rmtree(backs_dir)
    backs_dir.mkdir(parents=True)

    # Get direct subfolders only, sorted for consistent ordering
    subfolders = sorted(
        p for p in pokemon_dir.iterdir()
        if p.is_dir()
    )

    index = 1
    copied = 0
    for subfolder in subfolders:
        back_src = subfolder / "back.png"
        if not back_src.is_file():
            continue
        dest_name = f"back{index:04d}.png"
        dest_path = backs_dir / dest_name
        shutil.copy2(back_src, dest_path)
        if not resize_nearest(dest_path, TARGET_SIZE):
            print(f"Warning: failed to resize {dest_name} (ImageMagick installed?)")
        txt_path = backs_dir / f"back{index:04d}.txt"
        txt_path.write_text(BACK_CAPTION, encoding="utf-8")
        print(f"{back_src.relative_to(project_root)} -> backs/{dest_name} ({TARGET_SIZE[0]}x{TARGET_SIZE[1]})")
        index += 1
        copied += 1

    print(f"\nDone: copied and upscaled {copied} files to {backs_dir.relative_to(project_root)}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
