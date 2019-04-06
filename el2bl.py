#!/usr/bin/env python3
"""el2bl: convert Evernote internal relative note links to Bear note links"""
import os


def read_enex():
    """Read .enex files in directory:
    Accept path to directory from user input
    Verify that directory is valid with os.path.exists()
    Scan directory with os.scandir and create files object
    Run convert_links(files)
    """
    try:
        path = input("Please provide the file path to your Evernote exports: ")
        if os.path.exists(path):
            print(f"{path} is a valid directory.")
        files = os.scandir(path)
            convert_links(path, files)
    except:
        print("There was an error. Please try again.")


def convert_links(path, files):
    """Convert links in .enex files to Bear note link format:
    Create directory for converted files
    """
    if not os.path.exists(f"{path}/bear"):
        os.mkdir(f"{path}/bear")
    print("List of files:")
    for file in files:
        if file.name.endswith(".enex") and file.is_file():
            print(file)


if __name__ == "__main__":
    read_enex()
