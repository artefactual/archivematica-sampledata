#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pylint: disable=invalid-name

"""Global logging configuration for createtransfers.py."""

import logging
import logging.config  # Has to be imported separately


def setup(log_level, log_name):
    """Setup our logging with a number of constants and return a
    logger to the calling function.
    """

    # Log format string for flake8 compliance
    log_fmt = ('%(levelname)-8s  %(asctime)s%(filename)s:%(lineno)-4s '
               '%(message)s')

    # Configure logging
    config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': log_fmt,
                'datefmt': '%Y-%m-%d %H:%M:%S',
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
            },
        },
        'loggers': {
            'createtransfers': {
                'level': log_level,
                'handlers': ['console'],
            },
        },
    }

    logger = logging.getLogger(log_name)
    logging.config.dictConfig(config)
    return logger


def set_log_level(log_level, quiet, verbose):
    """Set the log level for this logger."""
    log_levels = {
        2: 'ERROR',
        1: 'WARNING',
        0: 'INFO',
        -1: 'DEBUG',
    }
    if log_level is None:
        level = quiet - verbose
        level = max(level, -1)  # No smaller than -1
        level = min(level, 2)  # No larger than 2
        return log_levels[level]
    return log_level
