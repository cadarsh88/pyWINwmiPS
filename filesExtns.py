import os
import sys
import csv
path = sys.argv[1]
with open('files.csv', 'w') as csvfile:
    fieldnames = ['File Name', 'Extension', 'File Path']
    writer = csv.DictWriter(csvfile, fieldnames)
    writer.writeheader()
    for root, directories, filenames in os.walk(path):
        for i in filenames:
	    if "." in i:
		f = i.split(".")
	    	writer.writerow({'File Name': i, 'Extension': f[1], 'File Path': root})