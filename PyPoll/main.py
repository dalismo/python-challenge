# modules to bring in
import os
import csv

# variables to hold datapoints
candidates = []
total_votes = 0 
vote_counts = []
election_data = ['1', '2']


# filepath 
election_csv = os.path.join('.','Resources','election_data.csv')

# Open and read the file using module
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes = total_votes + 1
# print(total_votes)
        candidate = row[2]
        print(candidate)

# # what is the vote percentage 
# for person, vote_count in candidates_votes.items():
#     candidates_percent[person] = '{0:.0%}'.format(vote_count / total_votes)
#     if vote_count > winner_votes:
#         winner_votes = vote_count
#         winner = person
# print(total_votes)







