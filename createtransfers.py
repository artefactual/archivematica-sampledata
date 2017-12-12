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


def create_large_test_transfers():
    """Create large test transfers by copying existing sampledata files
    multiple times to specific subdirectories of
    TestTransfers/acceptance-tests/performance/
    """
    performance_path = os.path.join(
        HERE, 'TestTransfers', 'acceptance-tests', 'performance')
    if os.path.exists(performance_path):
        shutil.rmtree(performance_path)
    os.makedirs(performance_path)

    # Create dir images-17M-each-2G-total/ containing 2G of 17M image files.
    image_path = os.path.join(
        HERE, 'TestTransfers', 'ManualNormalization', 'manualNormalization',
        'preservation', 'image_8.tif')
    n = 113
    images_dirname = 'images-17M-each-2G-total'
    images_path = os.path.join(performance_path, images_dirname)
    if os.path.exists(images_path):
        shutil.rmtree(images_path)
    os.makedirs(images_path)
    for i in range(n):
        new_image_fname = 'image_{}.tif'.format(i)
        new_image_path = os.path.join(images_path, new_image_fname)
        shutil.copyfile(image_path, new_image_path)

    # Create dir video-14M-each-10G-total/ containing 10G of 14M video files.
    video_path = os.path.join(
        HERE, 'SampleTransfers', 'Multimedia', 'MakeUp.mov')
    n = 669
    videos_dirname = 'video-14M-each-10G-total'
    videos_path = os.path.join(performance_path, videos_dirname)
    if os.path.exists(videos_path):
        shutil.rmtree(videos_path)
    os.makedirs(videos_path)
    for i in range(n):
        new_video_fname = 'video_{}.tif'.format(i)
        new_video_path = os.path.join(videos_path, new_video_fname)
        shutil.copyfile(image_path, new_video_path)


if __name__ == '__main__':
    COMMANDS = {
        'create-variously-encoded-files': create_variously_encoded_files,
        'create-large-test-transfers': create_large_test_transfers,
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
