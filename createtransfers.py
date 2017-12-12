#! /usr/bin/env python2
"""This executable creates Archivematica sample and/or test transfers.

Possible reasons for creating transfers dynamically instead of just including
them in the repository include:

1. The transfers are very large.
2. The transfers contain directories or files whose names are in non-standard
   encodings which can bork on certain platforms.

Usage:

"""

import argparse
import os
import shutil


HERE = os.path.dirname(os.path.abspath(__file__))


VARIOUS_ENCODINGS = (
    {
        'dir_name': 'windows_1252',
        'encoding': 'cp1252',
        'file_name': u's\xf8ster'
    }, {
        'dir_name': 'shift_jis',
        'encoding': 'shift-jis',
        'file_name': u'\u307d\u3063\u3077\u308b\u30e1\u30a4\u30eb'
    }, {
        'dir_name': 'big5',
        'encoding': 'big5',
        'file_name': u'\u5ee3\u5dde'
    }
)


def create_variously_encoded_files():
    """Create files with strange (non-UTF8) encodings under
    TestTransfers/files_with_various_encodings/
    """
    target_path = os.path.join(
        HERE, 'TestTransfers', 'files_with_various_encodings')
    for encoding_info in VARIOUS_ENCODINGS:
        encoding_dir_path = os.path.join(
            target_path, encoding_info['dir_name'])
        if os.path.exists(encoding_dir_path):
            shutil.rmtree(encoding_dir_path)
        os.makedirs(encoding_dir_path)
        encoding = encoding_info['encoding']
        file_name_unicode = encoding_info['file_name']
        file_name_bytes = file_name_unicode.encode(encoding)
        file_path_bytes = os.path.join(encoding_dir_path, file_name_bytes)
        with open(file_path_bytes, 'w') as fout:
            fout.write('The name of this file is encoded with encoding'
                       ' {}\n'.format(encoding))


if __name__ == '__main__':
    COMMANDS = {
        'create-variously-encoded-files': create_variously_encoded_files,
    }
    description = (
        'Create Archivematica Transfers. Available commands:\n  {}'.format(
            '\n  '.join(COMMANDS)))
    parser = argparse.ArgumentParser(
        description=description, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('command')
    args = parser.parse_args()
    try:
        COMMANDS[args.command]()
    except KeyError:
        print 'No such command: {}'.format(args.command)
