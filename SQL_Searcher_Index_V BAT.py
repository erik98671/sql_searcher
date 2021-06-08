#!/usr/bin/env python3
# SQL_Searcher_Class.py
# Last Updated 202103290818

import os
import time
import datetime
import SQL_Searcher_Class

# If this program starts on its own, run the main() function
if __name__ == "__main__":
    # Create the object
    tool = SQL_Searcher_Class.SQL_Searcher()
   
    # Creating index files
    root_folder = r"V:\Business Analysis Team"
    index_file_name = "index_files\sql_file_index_V BAT.txt"
    tool.create_index(root_folder, index_file_name)
