#!/usr/bin/env python3
# SQL_Searcher_Class.py
# Last Updated 202103290818

import SQL_Searcher_Class

# Create the object
tool = SQL_Searcher_Class.SQL_Searcher()

# Define the list index files
index_files = [r"H:\Source\Repos\sql_searcher\index_files\sql_file_index_2021.txt",
               r"H:\Source\Repos\sql_searcher\index_files\sql_file_index_2020.txt",
               r"H:\Source\Repos\sql_searcher\index_files\sql_file_index_2019.txt",
               r"H:\Source\Repos\sql_searcher\index_files\sql_file_index_2018.txt",
               r"H:\Source\Repos\sql_searcher\index_files\sql_file_index_2017.txt",
               r"H:\Source\Repos\sql_searcher\index_files\sql_file_index_2016.txt",
               r"H:\Source\Repos\sql_searcher\index_files\sql_file_index_2015.txt",
               r"H:\Source\Repos\sql_searcher\index_files\sql_file_index_V_BAT.txt"
               ]

#Define the search term
search_term = input("Search term: ")

# Run for each index file
print(f"Reading index: {index_files[0]}\n")
matches_list = tool.search_files(index_files[0], search_term) # 2021
for match in matches_list:
    with open(search_term + "_filelist.txt", "a") as output:
        output.write(match + "\n")

print(f"Reading index: {index_files[1]}\n")
matches_list = tool.search_files(index_files[1], search_term) # 2020
for match in matches_list:
    with open(search_term + "_filelist.txt", "a") as output:
        output.write(match + "\n")

print(f"Reading index: {index_files[2]}\n")
matches_list = tool.search_files(index_files[2], search_term) # 2019
for match in matches_list:
    with open(search_term + "_filelist.txt", "a") as output:
        output.write(match + "\n")
        
print(f"Reading index: {index_files[3]}\n")
matches_list = tool.search_files(index_files[3], search_term) # 2018
for match in matches_list:
    with open(search_term + "f_ilelist.txt", "a") as output:
        output.write(match + "\n")
        
print(f"Reading index: {index_files[4]}\n")
matches_list = tool.search_files(index_files[4], search_term) # 2017
for match in matches_list:
    with open(search_term + "_filelist.txt", "a") as output:
        output.write(match + "\n")
        
print(f"Reading index: {index_files[5]}\n")
matches_list = tool.search_files(index_files[5], search_term) # 2016
for match in matches_list:
    with open(search_term + "_filelist.txt", "a") as output:
        output.write(match + "\n")
        
print(f"Reading index: {index_files[6]}\n")
matches_list = tool.search_files(index_files[6], search_term) # 2015
for match in matches_list:
    with open(search_term + "_filelist.txt", "a") as output:
        output.write(match + "\n")
        
print(f"Reading index: {index_files[7]}\n")
matches_list = tool.search_files(index_files[7], search_term) # V Business Analyst Team
for match in matches_list:
    with open(search_term + "_filelist.txt", "a") as output:
        output.write(match + "\n")

hold_for_user = input("Done. Press the enter key to end.")
