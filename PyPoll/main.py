# modules to bring in
import os
import csv

# variables to hold datapoints
total_votes = 0
candidates = ""
candidates_votes = {}
candidates_percent = {}
winning_votes = 0
winner = ""

# filepath 
election_csv = os.path.join('.','Resources','election_data.csv')

# Open and read the file using module
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)

    for row in csvreader:
        total_votes = total_votes + 1
        candidates = row[2]
        if candidates in candidates_votes:
            candidate_place = candidates.index(candidates_name)
            condidate_votes[candidates] = condidate_votes[candidates] +1
        else:
            candidates_votes[condidates] = 1

# what is the vote percentage 


