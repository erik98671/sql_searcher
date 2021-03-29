#!/usr/bin/env python3
# SQL_Search_Tool.py
# Last Updated 202001060930

import SQL_Searcher_Class

if __name__ == "__main__":
    root_folder = "" # Used for indexing

    index_file_name_list = [r"H:\Git\sql_searcher\index_files\sql_file_index_h_2021.txt",
                            r"H:\Git\sql_searcher\index_files\sql_file_index_h_2020.txt",
                            r"H:\Git\sql_searcher\index_files\sql_file_index_h_2019.txt"]
    
    output_file_name = "sql_search_results_"

    for index_file_name in index_file_name_list:
        print(f"Starting in directory {index_file_name}")
        tool = SQL_Searcher_Class.SQL_Searcher(root_folder, index_file_name, output_file_name)
        tool.write_match_list()
