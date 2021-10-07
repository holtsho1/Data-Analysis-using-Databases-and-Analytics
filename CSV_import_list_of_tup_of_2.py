def csv_import_list_of_tup_of_2(file):
	

	import csv

	with open('file.csv', newline='') as f:
    	reader = csv.reader(f)
    	data = [tuple(row) for row in reader]

	#print(data)
	return data
