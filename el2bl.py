#!/usr/bin/env python3
"""el2bl: convert Evernote note links to Bear note links"""

import pathlib
import re


def input_enex_path() -> None:
    """Read .enex files in directory.
    ---
    - Accept path to directory from user input
    - Verify that directory is valid
    - Iterate over directory and convert links in each file
    """
    input_path = input("Please input the path to a directory with Evernote exports: ")
    path = pathlib.Path(input_path)
    try:
        if not path.is_dir():
            raise NotADirectoryError(path)
        for file in path.iterdir():
            if file.is_file() and file.suffix == ".enex":
                convert_links(file)
    except Exception as e:
        print(f"\n{e.__class__.__qualname__}: {e}")


def convert_links(enex_path: pathlib.Path) -> pathlib.Path:
    """Convert links in .enex files to Bear note link format.
    ---
    - Read contents of file
    - Replace Evernote note link URIs, but not other URIs, with Bear note links
    - Remove H1 tags from note body
    - Write to a new file in the bear subdirectory
    """
    print(f"Converting {enex_path.name}...")
    enex_contents = enex_path.read_text()
    enex_contents_with_converted_links = re.sub(
        r'(<a.*?href="evernote.*?>)(.*?)(</a>?)', r"[[\2]]", enex_contents
    )
    enex_contents_with_converted_links = re.sub(
        r"(<h1.*?>)(.*?)(</h1>?)", r"\2", enex_contents_with_converted_links
    )
    new_enex_dir = enex_path.parent / "bear"
    new_enex_dir.mkdir(exist_ok=True)
    new_enex_path = new_enex_dir / enex_path.name
    new_enex_path.write_text(enex_contents_with_converted_links)
    print(f"Converted {enex_path.name}. New file available at {new_enex_path}.")
    return new_enex_path


if __name__ == "__main__":
    input_enex_path()
