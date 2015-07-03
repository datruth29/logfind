#! /usr/bin/env python3

from nose.tools import assert_raises, assert_list_equal, assert_true, assert_false
from logfind import logfind
import os


class TestFindlog(object):
    def setup(self):
        self.log_files = [os.path.join(os.path.dirname(__file__), 'data', 'test_logfile')]
        self.arguments_or = ['-o', 'this', 'is', 'a', 'test']
        self.arguments_and = ['this', 'is', 'a', 'test']

    def test_return_parsar(self):
        parser = logfind.return_parser()
        with assert_raises(SystemExit):
            parser.parse_args()
            parser.parse_args(['-o'])

    def test_search_files_using_or(self):
        print(self.log_files)
        files_found = logfind.search_files(self.log_files, self.arguments_or)
        assert_list_equal(files_found, self.log_files)

    def test_search_files_using_and(self):
        files_found = logfind.search_files(self.log_files, self.arguments_and)
        assert_list_equal(files_found, self.log_files)

    def test_find_words_using_or(self):
        parser = logfind.return_parser()
        parsed_arguments = parser.parse_args(self.arguments_or)
        assert_true(logfind.find_words(parsed_arguments, b'this is a test'))

    def test_find_words_using_or_fail(self):
        parser = logfind.return_parser()
        parsed_arguments = parser.parse_args(self.arguments_or)
        assert_false(logfind.find_words(parsed_arguments, b'blah blah blah'))

    def test_find_words_using_and(self):
        parser = logfind.return_parser()
        parsed_arguments = parser.parse_args(self.arguments_and)
        assert_true(logfind.find_words(parsed_arguments, b'this is a test'))

    def test_find_words_using_and_fail(self):
        parser = logfind.return_parser()
        parsed_arguments = parser.parse_args(self.arguments_and)
        assert_false(logfind.find_words(parsed_arguments, b'this is a '))
