# -*- coding: utf-8 -*-

import json
from os import rename
from argparse import (ArgumentParser, FileType)


__author__    = 'Kazuyuki TAKASE'
__copyright__ = 'PLEN Project Company Inc, and all authors.'
__license__   = 'The MIT License'


# The application entry point.
# =============================================================================
def main(args):
    for file in args.files:
        motion           = json.load(file)
        motion_file_name = file.name

        file.close()

        rename(motion_file_name, '{:02X}_{}.json'.format(motion['slot'], motion['name']).replace(' ', '_'))


# Parse command-line option(s).
# =============================================================================
if __name__ == '__main__':
    arg_parser = ArgumentParser()

    arg_parser.add_argument(
        '-f', '--files',
        dest     = 'files',
        type     = FileType('r', encoding='utf-8'),
        nargs    = '+',
        required = True,
        help     = 'Please set any motion files you would like to name from the motion property.'
    )

    args = arg_parser.parse_args()
    main(args)
