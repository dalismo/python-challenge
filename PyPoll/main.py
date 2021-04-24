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
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes = total_votes +1
        candidates_name = (row[2])
        if candidates_name in candidates:
            candidate_place = candidates.index(candidates_name)
            vote_count[candidate_place] = vote_count[candidate_place] +1