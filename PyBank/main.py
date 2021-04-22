# modules
import csv
import os

# filepath location
budget_csv = os.path.join('.','Resources','budget_data.csv')

#check on path
print(budget_csv)

# opening and reading the file
with open(budget_csv, 'r') as budget_csv:
    csvreader = csv.reader(budget_csv, delimiter=',')

# lists to contain counts/calcs
months = []
gainloss = []

# starting that great loop
for row in csvreader:
    month.append(row[1])
    profit.apend(int(row[1])
    

