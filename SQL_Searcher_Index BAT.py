#!/usr/bin/env python3
# SQL_Searcher_Class.py
# Last Updated 202103290818

import SQL_Searcher_Class

# Create the object
tool = SQL_Searcher_Class.SQL_Searcher()

# Creating index files
root_folder = r"V:\Business Analysis Team"
index_file_name = "index_files\sql_file_index_V_BAT.txt"
max_size = 1000000 # The large files have data in them, ignore those.

tool.create_index(root_folder, index_file_name, max_size)
