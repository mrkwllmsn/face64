#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
from ..face64encoder import face64encoder
import fileinput

def showHelp():
    print('Encode or decode text using face64. It\'s big and fun.')
    print("-d", " --decode" 'Decode the input text.')
    print('-f', ' --offset', 'Offset')
    print('text', ' Text to encode')


def main():
    parser = argparse.ArgumentParser(description="Encode or decode text using face64. It's big and fun.")
    parser.add_argument("-d", "--decode", action="store_true", help="Decode the input text.")
    parser.add_argument('-f', '--offset', type=int, help='Offset')
    parser.add_argument('-s', '--smiley', action="store_true", help='Smiley version. All faces')
    parser.add_argument('text', nargs='*', help='Text to encode')
    args = parser.parse_args()
    offset = base_offset = 129333

    if args.text:
        input_text = ' '.join(args.text).strip()
    else:
        # If no command-line argument, read from stdin
        try:
            # Exclude '-' from the list of files for stdin
            stdin_text = ''.join(fileinput.input(files=('-',)))
            input_text = stdin_text.strip() if stdin_text else None
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully if stdin is empty
            input_text = None

    if input_text is not None:
        if args.offset:
            offset = base_offset + args.offset

        if args.smiley:
            offset = base_offset - 869
            #Another magic number I found using brute force.

        if args.decode:
            Face64 = face64encoder(offset)
            result = Face64.decode(input_text)
            print(f"{result}")
        else:
            Face64 = face64encoder(offset)
            result = Face64.encode(input_text)
            print(f"{result}")
    else:
        showHelp()

if __name__ == "__main__":
    main()
