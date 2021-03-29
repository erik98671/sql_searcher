#!/usr/bin/env python3
# sql_searcher_indexer_v_bat.py
# Last Updated 202101050930

import SQL_Searcher_Class

if __name__ == "__main__":
    # Parameters and settings
    root_folder = r"V:\Business Analysis Team"
    index_file_name = "sql_file_index_v_bat.txt"
    output_file_name = ""

    # Create the object
    tool = SQL_Searcher_Class.SQL_Searcher(root_folder, index_file_name, output_file_name)

    # Create index
    tool.create_index()
