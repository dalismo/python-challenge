# modules to bring in
import os
import csv

# filepath 
budget_csv = os.path.join('.','Resources','budget_data.csv')

# check on path
print(budget_csv)

# variables to store for counts
total_months = 0
toal_gainloss = 0
greatestincrease_gainloss = 0
greatestdecrease_gainloss = 0

# Open and read the file using module
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


