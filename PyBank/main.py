# help creating filepath
import os

# module to read csv
import csv

#variables to storee
months_count = 0
total_gainloss = 0
change_gainloss = 0

#loop
    # where the file is located
    budgetpath = os.path.join("..","Resources","budget_data.csv")

# Open the CSV
with open(budgetpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

