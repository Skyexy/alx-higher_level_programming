#!/usr/bin/python3
"""
This is the LockedClass module
"""

class LockedClass(object):
    __slots__ = ['first_name']



    def __init__(self, first_name=""):
        self.first_name = first_name
