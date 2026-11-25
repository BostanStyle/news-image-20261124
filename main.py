#!/usr/bin/env python3
"""make.fun entry: world news of 24 November 2026, in one picture.

When the grader runs this file it places the picture that ships
alongside it into the output folder the grader names. Nothing is
downloaded, nothing is generated at run time, and the copy is
byte-for-byte the picture in this repository. The picture is
1024 by 1024 pixels and 106,063 bytes in this entry.
"""
from pathlib import Path
import os
import sys

MAX_IMAGE_BYTES = 1024 * 1024
EXPECTED_SIDE = 1024
PICTURE_NAME = "entry.png"


def picture_path() -> Path:
    return Path(__file__).resolve().parent / PICTURE_NAME


def destination_folder() -> Path:
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if chosen:
        return Path(chosen)
    return Path("/output")


def check_picture(path: Path) -> None:
    if not path.is_file():
        raise FileNotFoundError(f"missing bundled picture: {path}")
    size = path.stat().st_size
    if size > MAX_IMAGE_BYTES:
        raise ValueError(f"picture is {size} bytes, over the 1 MiB limit")
    if size == 0:
        raise ValueError("picture is empty")


def deliver() -> int:
    source = picture_path()
    check_picture(source)
    folder = destination_folder()
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / PICTURE_NAME
    target.write_bytes(source.read_bytes())
    target.chmod(0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(deliver())
