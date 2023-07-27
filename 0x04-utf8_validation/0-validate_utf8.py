#!/usr/bin/env python3
"""
Iterate through integers to check if valid utf8 validation
"""


def validUTF8(data):
    """Method to validate utf8"""
    for val in data:
        if type(val) is not int:
            return False
        if val > 255 or val < 0:
            return False
    return True
