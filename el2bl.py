#!/usr/bin/env python3
"""el2bl: convert Evernote internal relative note links to Bear note links"""
import os
import re
from pampy import match


def read_enex():
    """Read .enex files in directory:
    Accept path to directory from user input
    Verify that directory is valid with os.path.exists()
    Scan directory with os.scandir and create files object
    Create directory for converted files
    Run convert_links(files)
    """
    try:
        path = input("Please provide the file path to your Evernote exports: ")
        if os.path.exists(path):
            print(f"{path} is a valid directory.")
            files = os.scandir(path)
            if not os.path.exists(f"{path}/bear"):
                os.mkdir(f"{path}/bear")
            print("List of files:")
            for file in files:
                if file.name.endswith(".enex") and file.is_file():
                    print(f"File name: {file.name}")
                    convert_links(file)
    except Exception as e:
        print(f"An error occurred:\n{e}\nPlease try again.")


def convert_links(file):
    """Convert links in .enex files to Bear note link format:
    Read contents of file
    Match Evernote links with Pampy and re
    """
    try:
        contents = open(file).read()
        return match(
            contents,
            re.compile('(<a href="evernote.*?>)(.*)(<\/a>)'),
            lambda link_start, title, link_end: print(f"Title: {title}"),
        )
        # TODO: return all matches, not just one
        # TODO: convert <a href="evernote:///.*">title</a> to [[title]]
    except Exception as e:
        print(f"An error occurred when converting links:\n{e}\nPlease try again.")


if __name__ == "__main__":
    read_enex()
