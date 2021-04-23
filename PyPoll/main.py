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

