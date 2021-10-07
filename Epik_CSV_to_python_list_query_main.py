
#import sql and panda package for data manipulation

import sqlite3
import pandas as pd

sql_connect = sqlite3.connect('db_name.db')

#import csv file with names and create usable list of tuples
name_data=csv_import_list_of_tup_of_2(input('file.csv'))

#dictionary to save query results for key value of the last name
results={}
for name in name_data:
    query_last_name=name[1]
    cursor = sql_connect.cursor()
    query = "SELECT * FROM db_name WHERE "+query_last_name+";"
    results[name[1]] = cursor.execute(query).fetchall()
    pd.read_sql_query(query,sql_connect) #panda query run, not necessary?

sql_connect.close()

#write the dictionary to csv file using function
dict_to_csv(results)




#-------------------------Functions--------------------------------------


#https://www.geeksforgeeks.org/how-to-save-a-python-dictionary-to-a-csv-file/
def dict_to_csv(dictionary):
    with open('Names.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerow(dictionary)

def csv_import_list_of_tup_of_2(file):
	

    import csv

    with open('file.csv', newline='') as f:
    reader = csv.reader(f)
    data = [tuple(row) for row in reader]

    #print(data)
    return data
