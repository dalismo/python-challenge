# modules to bring in
import os
import csv

# filepath 
budget_csv = os.path.join('.','Resources','budget_data.csv')

# variables to store for counts, calcs and loop
total_months = 0
total_net_gainloss = 0
greatest_increase_gainloss = 0
greatest_decrease_gainloss = 0
total_gainloss = 0
prior_gainloss = 0
percent_gainloss = 0
difference = 0
difference_list = []

# Open and read the file using module
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    csv_header = next(csvreader)
   
    # variable to store rows
    firstrow = next(csvreader)

    # take the prior value from the firstrow
    prior_gainloss = int(firstrow[1])

    # start of the loop through the data
    for row in csvreader:
        total_months = total_months + 1
        total_gainloss = total_gainloss + int(row[1])
        percent_gainloss = int(row[1])
        difference = percent_gainloss - prior_gainloss
        difference_list.append(difference_list)
        prior_gainloss = percent_gainloss

        # conditionals
        if percent_gainloss > greatest_increase_gainloss:
            greatest_increase_gainloss = percent_gainloss
            mx_month = row(0)
        if percent_gainloss < greatest_decrease_gainloss:
            greatest_decrease_gainloss = percent_gainloss
            mn_month = row(0)



