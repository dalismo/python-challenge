# modules to bring in
import os
import csv

# filepath 
budget_csv = os.path.join('.','Resources','budget_data.csv')

# check on path
print(budget_csv)

# variables to store for counts, calcs and loop
total_months = 0
toal_gainloss = 0
greatest_increase_gainloss = 0
greatest_decrease_gainloss = 0
total_gainloss = 0
prior_gainloss = 0
change_gainloss = 0
difference = 0
difference_list = []


# Open and read the file using module
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


