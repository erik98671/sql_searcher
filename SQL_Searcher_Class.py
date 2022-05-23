#!/usr/bin/env python3
# SQL_Searcher_Class.py
# Last Updated 202103290818

import os
import time
import datetime

class SQL_Searcher:
    def __init__(self):
        pass

    def create_index(self, root_folder, index_file_name, max_size):
        with open(index_file_name, "w") as output_file:
            for root, dirs, files in os.walk(root_folder):
                for file in files:
                    if file.endswith("sql"):
                        file_time = time.ctime(os.path.getmtime(os.path.join(root, file)))
                        file_size = os.stat(os.path.join(root, file)).st_size
                        file_name = os.path.join(root, file)

                        if file_size < max_size:
                            output_text = f"{file_time}\t{file_size}\t{file_name}\n"
                            output_file.write(output_text)

    def search_files(self, index_file_name, search_term):
        match_list = list() # The object to return

        with open(index_file_name, "r") as file:
            data = file.readlines()

            for line in data:
                found_match = False
                fields = line.split("\t")
                file_name_path = fields[2].replace("\n", "")

                with open(file_name_path, "r") as sql_file:
                    sql_data = sql_file.readlines()
                    
                    for sql_line in sql_data:
                        if search_term.upper() in sql_line.upper():
                            found_match = True
                            break
                            
                if found_match == True:
                    field_formatted = line.replace("\n", "")
                    match_list.append(field_formatted)
                    print(f"Found match in file {fields[2]}")

        return match_list       

# If this program starts on its own, run the main() function
if __name__ == "__main__":
    # Create the object
    tool = SQL_Searcher()
   
    # Creating index files
##    root_folder = r"H:\Timeline\2021"
##    index_file_name = "index_files\sql_file_index_2021.txt"
##    max_size = 1000000 # The large files have data in them, ignore those.
##    tool.create_index(root_folder, index_file_name, max_size)

    # Search index files
    index_files = [r"H:\Source\Repos\sql_searcher\index_files\sql_file_index_2021.txt",
                   r"H:\Source\Repos\sql_searcher\index_files\sql_file_index_2020.txt",
                   r"H:\Source\Repos\sql_searcher\index_files\sql_file_index_2019.txt",
                   r"H:\Source\Repos\sql_searcher\index_files\sql_file_index_2018.txt",
                   r"H:\Source\Repos\sql_searcher\index_files\sql_file_index_2017.txt",
                   r"H:\Source\Repos\sql_searcher\index_files\sql_file_index_2016.txt",
                   r"H:\Source\Repos\sql_searcher\index_files\sql_file_index_2015.txt"]

    search_term = "last claim"
    
    tool.search_files(index_files[0], search_term)
    tool.search_files(index_files[1], search_term)
    tool.search_files(index_files[2], search_term)
    tool.search_files(index_files[3], search_term)
    tool.search_files(index_files[4], search_term)
    tool.search_files(index_files[5], search_term)
    tool.search_files(index_files[6], search_term)
