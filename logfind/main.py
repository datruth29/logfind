#! /usr/bin/env python3

import sys
import os
import re
import fileinput


def search_files(log_files, regex_expression):
    files = []

    with fileinput.input(files=log_files) as f:
        for line in f:
            if re.search(regex_expression, line):
                # print("{0} in file {1}".format(line, fileinput.filename()))
                # print(fileinput.filename())
                files.append(fileinput.filename())
                fileinput.nextfile()
    return files


if __name__ == '__main__':
    # TODO: Make a configuration file to handle file names and directory information
    user_directory = os.path.expanduser('~')
    logfind_file = os.path.join(user_directory, '.logfind')

    with open(logfind_file, 'r') as f:
        # TODO: Don't include empty lines into the list
        log_files = f.read().splitlines()

    # print(lines)
    # TODO: Convert to Try/Except
    if not os.path.isfile(logfind_file):
        sys.exit("No .logfind file exists. Please create one.")

    # TODO: Check if the files in the .logfind file exist
    search_words = sys.argv[1:]
    if not search_words:
        sys.exit("No arguments were entered. Please enter arguments.")

    # print(search_words)
    regex_expression = "(" + ")|(".join(search_words) + ")"

    files_found = search_files(log_files, regex_expression)
    print('\n'.join('{}'.format(f) for f in files_found))
