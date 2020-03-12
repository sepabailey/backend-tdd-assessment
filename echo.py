#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "Sean Bailey, Koren Niles, Chris Wilson, Kano Marvel, Piero"


import argparse


def create_parser(*args):
    """Defines and provides help for commandline arguments"""
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    parser.add_argument("text",
                        type=str,
                        help="text to be manipulated")
    parser.add_argument('-u',
                        '--upper',
                        action='store_const',
                        const=bool,
                        help="convert text to uppercase")
    parser.add_argument("-l",
                        "--lower",
                        action='store_const',
                        const=bool,
                        help="convert text to lowercase")
    parser.add_argument("-t",
                        "--title",
                        action='store_const',
                        const=bool,
                        help="convert text to titlecase")
    return parser


def main():
    """Implementation of echo"""

    args = create_parser().parse_args()
    result = args.text

    if args.upper:
        result = result.upper()

    if args.lower:
        result = result.lower()

    if args.title:
        result = result.title()

    print(result)


if __name__ == '__main__':
    main()
