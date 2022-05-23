#
#
#

import SQL_Searcher_Class

# Create the object
tool = SQL_Searcher_Class.SQL_Searcher()

# Creating index file
root_folder = r"H:\Timeline\2022"
index_file_name = "index_files\sql_file_index_2022.txt"
max_size = 1000000 # The large files have data in them, ignore those.

tool.create_index(root_folder, index_file_name, max_size)
