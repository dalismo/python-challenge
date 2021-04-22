# modules
import csv
import os

budget_csv = os.path.join('.','Resources','budget_data.csv')
print(budget_csv)
with open(budget_csv, 'r') as budget_csv:
    csvreader = csv.reader(budget_csv, delimiter=',')

