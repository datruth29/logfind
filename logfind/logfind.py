#! /usr/bin/env python3

import sys
import os
import re
import fileinput
import argparse


def search_files(log_files, arguments):
    parser = return_parser()
    parsed_arguments = parser.parse_args(arguments)
    files = []

    with fileinput.input(files=log_files) as f:
        for line in f:
            if search_method(parsed_arguments, line):
                # print("{0} in file {1}".format(line, fileinput.filename()))
                # print(fileinput.filename())
                files.append(fileinput.filename())
                fileinput.nextfile()
    return files


def search_method(parsed_arguments, line):
    if parsed_arguments.o:
        regex = "(\\b" + "\\b|\\b".join(parsed_arguments.search_words) + "\\b)"
    else:
        # NOTE: This is a long operation. Perhaps use any and all instead?
        regex = "(?=.*\\b" + "\\b)(?=.*\\b".join(parsed_arguments.search_words) + "\\b)"
    return re.search(regex, line)


def return_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", help="perform an OR search", action="store_true")
    parser.add_argument("search_words", help="words that will be searched for", nargs='+')
    return parser


def main(arguments):
    # TODO: Make a configuration file to handle file names and directory information
    user_directory = os.path.expanduser('~')
    logfind_file = os.path.join(user_directory, '.logfind')

    with open(logfind_file, 'r') as f:
        # TODO: Don't include empty lines into the list
        log_files = f.read().splitlines()

    if not os.path.isfile(logfind_file):
        sys.exit("No .logfind file exists. Please create one.")

    # TODO: Check if the files in the .logfind file exist

    files_found = search_files(log_files, arguments)
    print('\n'.join('{}'.format(f) for f in files_found))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
