#!/usr/bin/env python3
# SQL_Searcher_Class.py
# Last Updated 202103290818

import os
import time
import datetime

class SQL_Searcher:
    def __init__(self, root_folder, index_file_name, output_file_name):
        self.root_folder = root_folder
        self.index_file_name = index_file_name
        self.output_file_name = output_file_name

    def create_index(self):
        print(f"{self.ts()} - Started creating index.")
        output_file = open('index_files/' + self.index_file_name, "w")
    
        for root, dirs, files in os.walk(self.root_folder):
            for file in files:
                if file[-3:].upper() == str("SQL"):
                    file_time = time.ctime(os.path.getmtime(os.path.join(root, file)))
                    file_date = str(datetime.datetime.strptime(file_time, "%a %b %d %H:%M:%S %Y"))
                    output_file.write(str(file_date[0:10]) + "\t" + os.path.join(root, file) + "\n")

        print(f"{self.ts()} - Finished creating index.")

    def get_user_input(self):
        user_input = input("What are you searching for: ")
        return user_input

    def search_files(self):
        match_list = list() # The object to return
        user_input = self.get_user_input() # The object to return
        
        print(f"{self.ts()} - Started searching.")
        with open(self.index_file_name, "r") as file:
            data = file.readlines()

            for line in data:
                found_match = False
                fields = line.split("\t")
                filename_truncated = fields[1][:-1]

                with open(filename_truncated, "r") as sql_file:
                    sql_data = sql_file.readlines()
                    
                    for sql_line in sql_data:
                        if user_input.upper() in sql_line.upper():
                            found_match = True
                            next
                            
                if found_match == True:
                    field_formatted = fields[1].replace("\n", "")
                    match_list.append(field_formatted)
                    print(f"Found match in file {fields[1]}")

        print(f"{self.ts()} - Finished searching.")
        return match_list, user_input

    def write_match_list(self):
        match_list, user_input = self.search_files()
        
        print(f"{self.ts()} - Started writing output.")
        output_file = open(self.output_file_name + "_" + user_input + ".txt", "a")
    
        for match in match_list:
            output_file.write(match + "\n")

        output_file.close()
        print(f"{self.ts()} - Finished writing output.")

    def ts(self):
        return datetime.datetime.now().strftime("%H:%M:%S")

# If this program starts on its own, run the main() function
if __name__ == "__main__":
   
    # Parameters and settings
    root_folder = r"H:\Timeline\2020"    
    index_file_name = "sql_file_index_2020.txt"
    output_file_name = "sql_search_results_"

    # Create the object
    tool = SQL_Searcher(root_folder, index_file_name, output_file_name)

    create_index = True # Change this to True to create an index file
    
    if create_index == True:
        tool.create_index()
    else:
        tool.write_match_list()
    

