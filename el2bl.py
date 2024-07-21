#!/usr/bin/env python3
"""el2bl: convert Evernote note links to Bear note links"""
import os
import re


def input_enex_path():
    """Read .enex files in directory.
    ---
    - Accept path to directory from user input
    - Verify that directory is valid with os.path.exists()
    - Scan directory with os.scandir and create files object
    - Create directory for converted files
    - Run function to convert links in each file
    """
    path = input("Please input the path to a directory with Evernote exports: ")
    if not os.path.exists(path):
        print(f"Not a valid file path:\n{path}")
        return
    else:
        print(f"Valid file path: {path}")
    if not os.path.exists(f"{path}/bear"):
        os.mkdir(f"{path}/bear")
    for file in os.scandir(path):
        if file.is_file() and file.name.endswith(".enex"):
            convert_links(file)


def convert_links(file):
    """Convert links in .enex files to Bear note link format.
    ---
    - Read contents of file
    - Replace Evernote note link URIs, but not other URIs, with Bear note links
    - Remove H1 tags from note body
    - Write to a new file in the bear subdirectory
    """
    try:
        print(f"Converting {file.name}...")
        with open(file) as enex:
            enex_contents = enex.read()
            enex_contents_with_converted_links = re.sub(
                r'(<a.*?href="evernote.*?>)(.*?)(</a>?)', r"[[\2]]", enex_contents
            )
            enex_contents_with_converted_links = re.sub(
                r"(<h1.*?>)(.*?)(</h1>?)", r"\2", enex_contents_with_converted_links
            )
            with open(f"{os.path.dirname(file)}/bear/{file.name}", "x") as new_enex:
                new_enex.write(enex_contents_with_converted_links)
            print("Done. New file available in the bear subdirectory.")
    except Exception as e:
        print(f"An error occurred:\n{e}\nPlease try again.")


if __name__ == "__main__":
    input_enex_path()
