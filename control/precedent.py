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

from pickle import dump,load,HIGHEST_PROTOCOL
from pdf2image import convert_from_path
from skimage.feature import match_template
from tabula import read_pdf_with_template

class Precedent(object):
    def __init__(self, name, dfs, path_to_pdf, column_aliases_matrix*):
        self.name = name                     # "{First word in filename}{Year}"
        self.aliases = column_aliases_matrix # Pass different column names
        self.dfs = dfs
        self.pdf = path_to_pdf
    def preserve(self):
        with open('../data/precedents/'+name+'.pkl','wb') as file_out:
            dump(self,file_out,HIGHEST_PROTOCOL)
    def compare(self,path_to_other_pdf):
        this_template = p2i.convert_from_path(self.pdf)
        other_image = p2i.convert_from_path(path_to_other_pdf)
        return match_template(other_image,this_template)
    def convert_using_template(self,template_path):
        return 
        
def generate_name(filename):
    words = filename.split('_')
    numerics = ["0","1","2","3","4","5","6","7","8","9"]
    temp = ''
    year = ''
    name = ''
    for word in words:
        if numerics in word:
            for i in range(len(word)):
                if word[i] in numerics:
                    temp = temp + word[i]
                    word.replace(word[i],"",1)
            if len(temp) >= 4:
                year = temp
            if len(word) > 0:
                for char in word:
                    name = name + char
        else:
            name = word
            year = 'na'
    return name + "_" + year