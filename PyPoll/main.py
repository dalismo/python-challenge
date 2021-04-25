import os
import csv

# Import CSV here
election_csv = os.path.join('.','Resources','election_data.csv')
print(election_csv)

# variables to store
Candidates = []
Khan = 0
Correy = 0
Li = 0
OTooley = 0
VoteCount = []
number_votes = 0


# opening and reading the file
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        number_votes = number_votes +1
        # candidate who was voted for
        candidate = row[2]
        Candidates.append(candidate)
        # conditional for loop
        if candidate == "Khan":
            Khan = Khan + 1
        elif candidate == "Correy":
            Correy = Correy + 1
        elif candidate == "Li":
            Li = Li +1
        elif candidate == "O'Tooley":
            OTooley = OTooley + 1
    winner = min(Candidates)
    percent_Khan = (Khan * 100)/ number_votes
    percent_Correy = (Correy*100)/ number_votes
    percent_Li= (Li*100)/ number_votes
    percent_OTooley = (OTooley*100)/ number_votes
    
    print(Khan)
    print(number_votes)
    print(percent_Khan)
    print(percent_Correy)
    print(percent_Li)
    print(percent_OTooley)
    print(winner)

# print("Election Results are in!")
# print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
# print("Total Votes: " + str(rowcount))
# print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")


    
# print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")
# print("Winner: " + str(WinnersName))
# print("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-")

# with open("election_results.txt", "w") as output:
# 	output.write("Election Results are in!\n")
# 	output.write("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-\n")
# 	output.write("Total Votes: " + str(rowcount) + "\n")
# 	output.write("~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-\n")
















































