#****************************************************************
# Filename: cache.py
# Author: Milan Donhowe
# Date: 6/14/2020
# Description:  Queue data-structure intended to prevent repeat
#               strategies from being picked as frequently
#****************************************************************

class Cache(object):
    def __init__(self, size):
        self.size = size;
        self.ls = list()

    def add(self, strat):
        if (len(self.ls) >= self.size):
            self.ls.pop()
        self.ls.insert(0, strat)

    def __contains__(self, key):
        return key in self.ls