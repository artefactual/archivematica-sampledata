#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# pylint: disable=invalid-name

"""Handler for the createtransfers.py script arguments."""
import argparse
from collections import namedtuple

# Default arguments for deep-transfers. These arguments are closest to the
# values that initiated the generation of this code for testing upon failure.
DEFAULT_DEPTH = 5
DEFAULT_NUMBER_DIRS = 3
DEFAULT_NUMBER_FILES = 4


def get_parser(**kwargs):
    """Argument parsing configuration for the CLI."""

    # Reusable option constants (for CLI).
    Opt = namedtuple('Opt', ['name', 'metavar', 'help', 'default', 'type'])
    depth = Opt(
        name='recursion-depth',
        metavar='INT',
        help='Depth of directory structure to create. '
             'Default depth: {0}.'.format(DEFAULT_DEPTH),
        default=DEFAULT_DEPTH,
        type=int)
    nodirs = Opt(
        name='number-of-directories',
        metavar='INT',
        help='Number of sub-directories per depth. '
             'Default {0} directories.'.format(DEFAULT_NUMBER_DIRS),
        default=DEFAULT_NUMBER_DIRS,
        type=int)
    nofiles = Opt(
        name='number-of-files',
        metavar='INT',
        help='Number of files per sub-directory. '
             'Default {0} files.'.format(DEFAULT_NUMBER_FILES),
        default=DEFAULT_NUMBER_FILES,
        type=int)

    # Sub-command configuration: give them a name, help text, a tuple of
    # ``Arg`` instances and a tuple of ``Opts`` instances.
    Subcommand = namedtuple('SubCommand', ['name', 'help', 'args', 'opts'])
    subcommands = (
        Subcommand(
            name=kwargs["CMD_ENCODINGS"],
            help='Create sample data with variously encoded filenames and '
                 'strange characters.',
            args=None,
            opts=None
        ),
        Subcommand(
            name=kwargs["CMD_LARGE"],
            help='Create large transfer sample data.',
            args=None,
            opts=None
        ),
        Subcommand(
            name=kwargs["CMD_DEEP"],
            help='Create sample data with some level of filesystem structure. '
                 'For example, consisting of lots of directories of a certain '
                 'depth.',
            args=None,
            opts=(depth, nodirs, nofiles)
        ),
    )

    parser = argparse.ArgumentParser(
        description='Create Archivematica Transfers. Available commands:',
        formatter_class=argparse.RawDescriptionHelpFormatter)

    subparsers = parser.add_subparsers(help='sub-command help',
                                       dest='subcommand', metavar="<command>")
    for subcommand in subcommands:
        subparser = subparsers.add_parser(subcommand.name,
                                          help=subcommand.help)
        if subcommand.args is not None:
            for arg in subcommand.args:
                subparser.add_argument(
                    arg.name, help=arg.help, type=arg.type)

        if subcommand.opts is not None:
            for sub_arg in subcommand.opts:
                subparser.add_argument(
                    '--' + sub_arg.name,
                    metavar=sub_arg.metavar,
                    help=sub_arg.help,
                    default=sub_arg.default,
                    type=sub_arg.type)
    return parser
