#!/usr/bin/env python3
"""el2bl: convert Evernote internal relative note links to Bear note links"""
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
        path = input("Please provide the file path to your Evernote exports: ")
        if os.path.exists(path):
            print(f"Valid file path: {path}")
            if not os.path.exists(f"{path}/bear"):
                os.mkdir(f"{path}/bear")
            for file in os.scandir(path):
                if file.name.endswith(".enex") and file.is_file():
                    convert_links(file)
        else:
            print(f"Not a valid file path:\n{path}")
    except Exception as e:
        print(f"An error occurred:\n{e}\nPlease try again.")


def convert_links(file):
    """Convert links in .enex files to Bear note link format.

    - Read contents of file with Beautiful Soup
    - Identify note link URIs, but not other URIs
    - Replace Evernote note links with Bear note links
    - Write to a new file in the bear subdirectory
    """
    with open(file) as enex:

        def note_link(href):
            """Identify note link URIs using href attribute and regex"""
            return href and re.compile(r"evernote://").search(href)

        soup = BeautifulSoup(enex, "lxml")
        for link in soup.find_all(href=note_link):
            string = link.string.extract()
            bear_link = link.replace_with(f"[[{string}]]")
        with open(f"{os.path.dirname(file)}/bear/{file.name}", "x") as new_enex:
            new_enex.write(str(soup))


if __name__ == "__main__":
    input_enex_path()
