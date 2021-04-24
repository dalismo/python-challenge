# modules to bring in
import os
import csv

# filepath 
election_csv = os.path.join('.','Resources','election_data.csv')

# Open and read the file using module
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvfile)

#take the first row
firstrow = next(csvreader)

# vartiables to hold datapoints
total_cast = 0
candidates = {}
percent = {}
thewinner = ""
win_count = 0

# start of the loop
for row in csvreader:
    total_cast = total_cast +1