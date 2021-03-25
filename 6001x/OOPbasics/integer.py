# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 14:51:57 2021

@author: caear
"""

class inSet(object):
    """An inSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""
    
    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []
        
    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)
        
    def member(self, e):
        """Assumes e is an integer
        Return True if e is in self, and False otherwise"""
        return e in self.vals
    
    def remove(self, e):
        """Assumes e is an integer and removes e from self
        Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')
    def __str__(self):
        """Return a string representation of self"""
        self.vals.sort()
        result = ''
        for e in self.vals:
            result += str(e) + ','
        return '{' + result[:-1] + '}'