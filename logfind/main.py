#!/usr/bin/env python3

import sys
import os


if __name__ == '__main__':
    #TODO: Make a configuration file to handle file names and directory information
    user_directory = os.path.expanduser('~')
    logfind_file = os.path.join(user_directory, '.logfind')

    if not os.path.isfile(logfind_file):
        sys.exit("No .logfind file exists. Please create one.")

    search_words = sys.argv[1:]
    if not search_words:
        sys.exit("No arguments were entered. Please enter arguments.")
    else:
        print(search_words)
