#-------------------------Functions--------------------------------------


#https://www.geeksforgeeks.org/how-to-save-a-python-dictionary-to-a-csv-file/
def dict_to_csv(dictionary,field_names):
    #print(dictionary)
    with open('Names Output.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerow(dictionary)

def csv_import_list_of_tup_of_2(file):
	

    

    with open(file, newline='') as f:
        reader = csv.reader(f)
        data = [(row) for row in reader]

    #print(data)
    return data



#----------------------------------------------------------------------------


import csv


#import sql and panda package for data manipulation

import sqlite3
import pandas as pd

import  tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
print(file_path)
#import csv file with names and create usable list of tuples
name_data=csv_import_list_of_tup_of_2(file_path)

#dictionary to save query results for key value of the last name
results={}
field_names=[]
test={"Name1":["First","Second","Third"],"Name2":["First1","Second1","Third1"],"Name3":["First2","Second2","Third2"],"Name4":["First3","Second3","Third3"],"Name6":["First4","Second4","Third4"],"Name2":["First5","Second5","Third5"]}
for name in name_data:
    if name[1] in test:
        print(results.keys())
        if name[1] in results.keys():
            for value in name[1]:
                results[name[1]].append(test[name[1]])
                print(results[name[1]])
                
        else:
            
            results[name[1]] = test[name[1]]
            if not results[name[1]]==[]:
                #name[1]=name[1].replace('\n','')
                field_names.append(name[1])


#write the dictionary to csv file using function
dict_to_csv(results,field_names)





