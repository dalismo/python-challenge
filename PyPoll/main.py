# modules to bring in
import os
import csv

# variables to hold datapoints
total_votes = 0 
candidate_vtd = {}
candidate_votes = 0
candiate_vtpercent={}
winner = ""


# filepath 
election_csv = os.path.join('.','Resources','election_data.csv')

# Open and read the file using module
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)

    for row in csvreader:
        if row[2] in candidate_vtd:
            candidate_vtd[row[2]] += 1
        else:
            candidate_vtd[row[2]] = 1
        total_votes = total_votes + 1
        winner = max(candidate_vtd, key=candidate_vtd.get)

vote_percentdict = {}
for key in candidate_vtd.keys():
    vote_list = []
    vote_list.append(candidate_vtd[key]/total_votes*100)
    vote_list.append(candidate_vtd[key])
    vote_percentdict[key] = vote_list

    







