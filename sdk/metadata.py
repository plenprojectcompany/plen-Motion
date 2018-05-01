# -*- coding: utf-8 -*-

import json
from argparse import (ArgumentParser, FileType)


__author__    = 'Kazuyuki TAKASE'
__copyright__ = 'PLEN Project Company Inc, and all authors.'
__license__   = 'The MIT License'


# Add metadata of the motion. (Automatically convert old schema to new schema.)
# =============================================================================
def process(motion, target, firmware):
    if '@metadata' not in motion:
        for code in motion['codes']:
            code['method']    = code.pop('func') if 'func' in code else code['method']
            code['arguments'] = code.pop('args') if 'args' in code else code['arguments']

    motion['@metadata'] = {
        'author': 'PLEN Project Company Inc.',
        'target': target,
        'required_firmware': firmware
    }

    motion['@frame_length'] = len(motion['frames'])

    for index, frame in enumerate(motion['frames']):
        frame['@index'] = index

    return motion


# The application entry point.
# =============================================================================
def main(args):
    for file in args.files:
        motion_processed = process(json.load(file), args.target, args.version)

        file.seek(0)
        json.dump(motion_processed, file, sort_keys=True, indent=4)
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
        help     = 'Please set any motion files you would like to add metadata.'
    )

    arg_parser.add_argument(
        '-t', '--target',
        dest     = 'target',
        default  = 'PLEN2',
        choices  = ('PLEN1.4', 'PLEN2', 'PLEN2 mini'),
        help     = 'Please set target robot.'
    )

    arg_parser.add_argument(
        '-v', '--firmware-version',
        dest     = 'version',
        default  = '1.4.1~',
        help     = 'Please set required firmware version of the target robot.'
    )

    args = arg_parser.parse_args()
    main(args)
