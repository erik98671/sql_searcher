#!/usr/bin/env python3
# SQL_Searcher_Class.py
# Last Updated 202103290818

import SQL_Searcher_Class

if __name__ == "__main__":
    tool = SQL_Searcher_Class.SQL_Searcher()

    index_files = [r"H:\Git\sql_searcher\index_files\sql_file_index_2021.txt",
                   r"H:\Git\sql_searcher\index_files\sql_file_index_2020.txt",
                   r"H:\Git\sql_searcher\index_files\sql_file_index_2019.txt",
                   r"H:\Git\sql_searcher\index_files\sql_file_index_2018.txt",
                   r"H:\Git\sql_searcher\index_files\sql_file_index_2017.txt",
                   r"H:\Git\sql_searcher\index_files\sql_file_index_2016.txt"]
   
    tool.search_files(index_files[1], "BSBS_TYPE")

