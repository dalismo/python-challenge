# modules to bring in
import os
import csv

# filepath 
budget_csv = os.path.join('.','Resources','budget_data.csv')

#check
print(budget_csv)


# variables to store for counts, calcs and loop
total_months = 0
total_net_gainloss = 0
greatest_increase_gainloss = 0
greatest_decrease_gainloss = 0
total_gainloss = 0
prior_gainloss = 0
amount_gainloss = 0
difference = 0
difference_list = []

# check 
print(total_months)

# Open and read the file using module
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
   
    # variable to store rows
    firstrow = next(csvreader)

    # take the prior value from the firstrow,[] is the index position
    prior_gainloss = int(firstrow[1])

    # check 
    print(prior_gainloss)
    
    # start of the loop through the data
    for row in csvreader:
        total_months = total_months +1
        total_gainloss = total_gainloss + int(row[1])
        amount_gainloss = int(row[1])
        difference = amount_gainloss - prior_gainloss
        difference_list.append(difference)
        prior_gainloss = amount_gainloss

        # conditionals
        if amount_gainloss > greatest_increase_gainloss:
            greatest_increase_gainloss = amount_gainloss
            mx_month = row[0]
        if amount_gainloss < greatest_decrease_gainloss:
            greatest_decrease_gainloss = amount_gainloss
            mn_month = row[0]

# check
print(total_months)
print(total_gainloss)

# time to get the average of changes in gain/loss over the whole period
theaverage = sum(difference_list)/total_months

# check
print(theaverage)

# time to print results to match view needed
print("Financial Analysis")
print("--------------------------------------------")
print("Total Months: {total_months}")
# print(f"Total: {total_gainloss}")
# print(f"Average Change: {theaverage}")
# print(f"Greatest Increase in Profits: {mx_month} {greatest_increase_gainloss}")
# print(f"Greatest Decrease in Profits: {mn_month} {greatest_decrease_gainloss}")

# # creating export file and writing to file results
# output = open("results.txt","w+")

# output.write("Financial Analysis \n")
# output.write("-------------------------------------------- \n")
# output.write(f"Total Months: {total_months} \n")
# output.write(f"Total: {total_gainloss} \n")
# output.write(f"Average Change: {theaverage} \n")
# output.write(f"Greatest Increase in Profits: {greatest_increase_gainloss} \n")
# output.write(f"Greatest Decrease in Profits: {greatest_decrease_gainloss} \n")







