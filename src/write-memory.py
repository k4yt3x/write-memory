#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: Write Memory
Author: K4YT3X
Date Created: October 18, 2019
Last Modified: October 19, 2019

Licensed under the GNU General Public License Version 3 (GNU GPL v3),
    available at: https://www.gnu.org/licenses/gpl-3.0.txt

(C) 2019 K4YT3X
"""

# built-in imports
import argparse

# local imports
from ip import IP


SUPPORTED_MODULES = [
    'ip'
]

IPROUTE2_OBJECTS = [
    'address',
    'route',
    'rule',
    'neigh'
]


def parse_arguments() -> argparse.Namespace:
    """ parse command line arguments
    
    Returns:
        argparse.Namespace -- parsed namespace
    """
    parser = argparse.ArgumentParser(prog='PROG', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    subparsers = parser.add_subparsers(title='module', help='sub-command help', required=True)

    iproute2 = subparsers.add_parser('ip', help='iproute2')
    iproute2.add_argument('object', help='object to interact with', choices=IPROUTE2_OBJECTS)

    actions_group = parser.add_mutually_exclusive_group(required=True)
    actions_group.add_argument('-s', '--show', help='show configurations in memory', action='store_true')
    actions_group.add_argument('-w', '--write', help='write memory to file', action='store_true')

    # parse arguments
    return parser.parse_args()


# this is not a library
if __name__ != '__main__':
    raise ImportError

# process command line arguments
args = parse_arguments()


if args.object == 'address':

    if args.show:
        import json
        for interface in IP.get_interface_configurations():
            print(json.dumps(interface.__dict__, indent=4))

else:
    print('this code should never be reached')
    print('please report this fatal error')
