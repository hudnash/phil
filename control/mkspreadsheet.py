#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MKSPREADSHEET.PY

Created on Wed Jun 22 12:25:52 2022

@author: hudsonnash
"""
import os
import tabula as tab
import re
import pandas as pd

def lamitan(udir):
    for file in os.listdir(udir):
        if os.path.splitext(file)[1] == '.pdf':
            dfs = tab.read_pdf(os.path.join(udir,file),lattice=True,pages='all')
            for df in dfs:
                df.rename(index={0: "x", 1: "y", 2: "z"})
            return pd.concat(dfs)
        
def fix_my_columns(dfs):
    def prompt_user_merge_cols(dfs):
        # TODO
        pass
    def same_column_names(dfs):
        # TODO 
        pass
    # Counts number of columns and if not same columns prompts user to merge which
    # columns.
    # Takes list of dataframes.
    smallest_col_num = len(dfs[0])
    largest col_num = len(dfs[0])
    for df in dfs:
        if len(df) < smallest_col_num:
            smallest_col_num = len(df)
        elif len(df) > largest_col_num:
            largest_col_num = len(df)
    if largest_col_num ~= smallest_col_num:
        prompt_user_merge_cols(dfs)
    elif same_column_names(dfs):
        # TODO: Then stuff
    return dfs
    
if __name__ == '__main__':
    # TODO : Classify the document as Lamitan format or Garden City format
    df = lamitan(os.path.join(os.path.dirname(os.getcwd()),'data/unzipped'))
    df.to_excel('test.xlsx')
    
