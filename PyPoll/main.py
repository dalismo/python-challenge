import os
import csv

# Import CSV here
election_csv = os.path.join('.','Resources','election_data.csv')
print(election_csv)

Candidates = []
VoteCount = []
rowcount = 0
Winner = 0
WinnersName = ""
i = 0

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

	
    for row in csvreader:
        rowcount = rowcount + 1
    print(rowcount)
	    if row[2] not in Candidates:
			Candidates.append(row[2])
# 			VoteCount.append(0)
# 	    else:
# 			VoteCount[Candidates.index(row[2])] = VoteCount[Candidates.index(row[2])] + 1

# Winner = max(range(len(VoteCount)), key = lambda x: VoteCount[x])
# WinnersName = Candidates[int(Winner)]

print("Election Results are in!")
print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
print("Total Votes: " + str(rowcount))
print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
    
print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
# print("Winner: " + str(WinnersName))
print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")

# i = 0

# with open("election_results.txt", "w") as output:
# 	output.write("Election Results are in!\n")
# 	output.write("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-\n")
# 	output.write("Total Votes: " + str(rowcount) + "\n")
# 	output.write("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-\n")






















