# modules to bring in
import os
import csv

# variables to hold datapoints
total_votes = 0
candidates = []
vote_count= []

# filepath 
election_csv = os.path.join('.','Resources','election_data.csv')

# Open and read the file using module
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvfile)

# start of the loop
    for row in csvreader: