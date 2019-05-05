#!/usr/bin/env python3
"""el2bl: convert Evernote note links to Bear note links"""
import os
import re
from bs4 import BeautifulSoup


def input_enex_path():
    """Read .enex files in directory.

    - Accept path to directory from user input
    - Verify that directory is valid with os.path.exists()
    - Scan directory with os.scandir and create files object
    - Create directory for converted files
    - Run function to convert links in each file
    """
    try:
        path = input("Please input the path to a directory with Evernote exports: ")
        if os.path.exists(path):
            print(f"Valid file path: {path}")
            if not os.path.exists(f"{path}/bear"):
                os.mkdir(f"{path}/bear")
            for file in os.scandir(path):
                if file.name.endswith(".enex") and file.is_file():
                    print("Converting files...")
                    convert_links(file)
                    print("Done. New files available in the bear subdirectory.")
        else:
            print(f"Not a valid file path:\n{path}")
    except Exception as e:
        print(f"An error occurred:\n{e}\nPlease try again.")


def convert_links(file):
    """Convert links in .enex files to Bear note link format.

    - Read contents of file with Beautiful Soup, and convert to string
    - Replace Evernote note link URIs, but not other URIs, with Bear note links
    - Remove H1 tags from note body
    - Write to a new file in the bear subdirectory
    """
    with open(file) as enex:
        soup = str(BeautifulSoup(enex, "html.parser"))
        soup_sub = re.sub(r'(<a href="evernote.*?>)(.*?)(</a>?)', r"[[\2]]", soup)
        soup_sub = re.sub(r"(<h1>?)(.*?)(</h1>?)", r"\2", soup_sub)
        with open(f"{os.path.dirname(file)}/bear/{file.name}", "x") as new_enex:
            new_enex.write(soup_sub)


if __name__ == "__main__":
    input_enex_path()
