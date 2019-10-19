#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: IP Controller
Author: K4YT3X
Date Created: October 18, 2019
Last Modified: October 19, 2019
"""

# built-in imports
import json
import pathlib
import subprocess

# local imports
from interface import Interface


# constants
IP_BINARY = pathlib.Path('/usr/sbin/ip')


class IP:
    """ ip command controller

    A high-level wrapper for iproute2's built-in ip command.
    This class controls ip command to retrieve interface and
    networking information.
    """

    @staticmethod
    def get_interface_configurations() -> list:
        """ get interfaces

        Get interface properties and create Interface objects for
        each of the interfaces.
        
        Returns:
            list -- list of Interface objects
        """

        # run ip address to get interface configurations
        ip_address_command = [IP_BINARY, '-j', 'a']
        ip_address_output = json.loads(subprocess.run(ip_address_command, stdout=subprocess.PIPE).stdout)

        # create list to hold all Interface objects
        interfaces = []

        # create an object and append it to the list for each interface
        for interface in ip_address_output:
            interface_object = Interface()
            interface_object.__dict__.update(interface)
            interfaces.append(interface_object)

        return interfaces
