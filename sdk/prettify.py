# -*- coding: utf-8 -*-

import json
from argparse import (ArgumentParser, FileType)


__author__    = 'Kazuyuki TAKASE'
__copyright__ = 'PLEN Project Company Inc, and all authors.'
__license__   = 'The MIT License'


# The application entry point.
# =============================================================================
def main(args):
    for file in args.files:
        motion = json.load(file)

        file.seek(0)
        json.dump(motion, file, sort_keys=True, indent=4)
        file.truncate()
        file.close()


# Parse command-line option(s).
# =============================================================================
if __name__ == '__main__':
    arg_parser = ArgumentParser()

    arg_parser.add_argument(
        '-f', '--files',
        dest     = 'files',
        type     = FileType('r+', encoding='utf-8'),
        nargs    = '+',
        required = True,
        help     = 'Please set any motion files you would like to name from the motion property.'
    )

    args = arg_parser.parse_args()
    main(args)
