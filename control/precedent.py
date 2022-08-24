#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PRECEDENT.PY

Created on Wed Aug 24 10:51:29 2022

@author: hudsonnash

OBJECTIVE: Handle operations concerning Precedent objects
            - class Precedent
            - Pickling
            - With folder-level and table-level Precedent instantiation in
              mind
"""

from pickle import # TODO

class Precedent(object):
    def __init__(self, name, column_aliases_matrix*):
        self.name = name                     # "{First word in filename}{Year}"
        self.aliases = column_aliases_matrix # Pass different column names
        
def generate_name()