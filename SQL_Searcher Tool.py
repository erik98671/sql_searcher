#
#
#

import SQL_Searcher_Class

# Create the object
tool = SQL_Searcher_Class.SQL_Searcher()

# Define the list index files
index_files = [r"H:\Source\Repos\SQL Searcher\index_files\sql_file_index_2022.txt",
               r"H:\Source\Repos\SQL Searcher\index_files\sql_file_index_2021.txt",
               r"H:\Source\Repos\SQL Searcher\index_files\sql_file_index_2020.txt",
               r"H:\Source\Repos\SQL Searcher\index_files\sql_file_index_2019.txt",
               r"H:\Source\Repos\SQL Searcher\index_files\sql_file_index_2018.txt",
               r"H:\Source\Repos\SQL Searcher\index_files\sql_file_index_2017.txt",
               r"H:\Source\Repos\SQL Searcher\index_files\sql_file_index_2016.txt",
               r"H:\Source\Repos\SQL Searcher\index_files\sql_file_index_2015.txt",
               r"H:\Source\Repos\SQL Searcher\index_files\sql_file_index_V_BAT.txt"]

#Define the search term
search_term = input("Search term: ")

print(f"Reading index: {index_files[0]}\n")
tool.search_files(index_files[0], search_term) # 2022

print(f"Reading index: {index_files[1]}\n")
tool.search_files(index_files[1], search_term) # 2021

print(f"Reading index: {index_files[2]}\n")
tool.search_files(index_files[2], search_term) # 2020

print(f"Reading index: {index_files[3]}\n")
tool.search_files(index_files[3], search_term) # 2019

print(f"Reading index: {index_files[4]}\n")
tool.search_files(index_files[4], search_term) # 2018

print(f"Reading index: {index_files[5]}\n")
tool.search_files(index_files[5], search_term) # 2017

print(f"Reading index: {index_files[6]}\n")
tool.search_files(index_files[6], search_term) # 2016

print(f"Reading index: {index_files[7]}\n")
tool.search_files(index_files[7], search_term) # 2015

#print(f"Reading index: {index_files[8]}\n")
#tool.search_files(index_files[8], search_term) # V Business Analyst Team

hold_for_user = input("Done")
