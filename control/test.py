#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TEST.PY

Created on Wed Aug 24 11:30:46 2022

@author: hudsonnash

OBJECTIVE: General-purpose test for phil Python files development
"""

import precedent as p
import clean_dump_to_dir as clean
import os.path

_dir = os.path.dirname(os.path.dirname(__file__))
zipped_dir = os.path.join(_dir,'data','zip')
unzipped_dir = os.path.join(_dir,'data','unzipped')
clean.unzip(zipped_dir,unzipped_dir)
try:
    clean.rem_unwanted_data(unzipped_dir)
except('NoPrecedentError'):
    
    
