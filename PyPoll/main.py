# modules to bring in
import os
import csv

# filepath 
election_csv = os.path.join('.','Resources','election_data.csv')
print(election_csv)

# Open and read the file using module
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    csv_header = next(csvfile)

#take the first row
firstrow = next(csvreader)

# vartiables to hold datapoints
total_cast = 0
candidates = {}
percent = {}
thewinner = ""
win_count = 0







