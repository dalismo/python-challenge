import os
import csv

#reading the file
csvpath = os.path.join ('Resources','budget_data.csv')

with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    print (csvreader)