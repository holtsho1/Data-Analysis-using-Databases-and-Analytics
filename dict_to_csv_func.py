#https://www.geeksforgeeks.org/how-to-save-a-python-dictionary-to-a-csv-file/
def dict_to_csv(dictionary):
    with open('Names.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerow(dictionary)
