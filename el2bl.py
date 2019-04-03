#!/usr/bin/env python3
"""el2bl: convert Evernote internal relative note links to Bear note links"""
import os


def read_enex():
    """Read .enex files in directory
    """
    try:
        path = input("Please provide the file path to your Evernote exports: ")
        print(path)
        # Read list of .enex files in directory.
        files = os.scandir(path)
        convert_links(files)
    except:
        print("Please try again, and enter a valid file path.")


def convert_links(files):
    """Convert links in .enex files to Bear note link format
    """
    print("List of files:")
    for file in files:
        if file.name.endswith(".enex") and file.is_file():
            print(file)


if __name__ == "__main__":
    read_enex()
