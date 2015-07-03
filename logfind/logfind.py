#! /usr/bin/env python3

import sys
import os
import re
import argparse
import mmap


def search_files(log_files, arguments):
    parser = return_parser()
    parsed_arguments = parser.parse_args(arguments)
    files = []

    for log_file in log_files:
        try:
            with open(log_file, 'r') as f:
                with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
                    if find_words(parsed_arguments, m):
                        files.append(log_file)
        except FileNotFoundError as e:
            print(e)
            next
    return files


def find_words(parsed_arguments, text):
    boundery = lambda s: b'\\b' + s + b'\\b'

    if parsed_arguments.o:
        regex = parsed_arguments.search_words
        result = any(re.search(boundery(word), text) for word in regex)
    else:
        regex = parsed_arguments.search_words
        result = all(re.search(boundery(word), text) for word in regex)
    return result


def return_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", help="perform an OR search", action="store_true")
    parser.add_argument("search_words", help="words that will be searched for", nargs='+',
                        type=lambda x: x.encode('utf-8'))
    return parser


def main(arguments):
    # TODO: Make a configuration file to handle file names and directory information
    user_directory = os.path.expanduser('~')
    logfind_file = os.path.join(user_directory, '.logfind')

    if not os.path.isfile(logfind_file):
        sys.exit("No .logfind file exists. Please create one.")

    with open(logfind_file, 'r') as f:
        log_files = list(filter(None, f.read().splitlines()))

    files_found = search_files(log_files, arguments)
    print('\n'.join('{}'.format(f) for f in files_found))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
