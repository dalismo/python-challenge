git # modules to bring in
import os
import csv

# filepath 
budget_csv = os.path.join('.','Resources','budget_data.csv')

# variables to store for counts, calcs and loop
total_months = []
total_net_gainloss = 0
total_gainloss = 0
prior_gainloss = 0
amount_gainloss = 0
amt_gainloss = []
difference = 0
difference_list = []
max_month = 0
min_month = 0


# # check 
# print(total_months)

# Open and read the file using module
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
   
    # variable to store rows
    # firstrow = next(csvreader)

    # take the prior value from the firstrow,[] is the index position


    # check 
    # print(prior_gainloss)
    
    # start of the loop through the data
    for row in csvreader:
        total_months.append(row[0])
        total_gainloss = total_gainloss + int(row[1])
        amount_gainloss = int(row[1])
        difference = amount_gainloss - prior_gainloss
        if prior_gainloss == 0:
            difference = 0
        difference_list.append(difference)
        prior_gainloss = amount_gainloss
    theaverage= sum(difference_list)/(len(total_months)-1)
    new_month = (len(total_months))
    highest = max(difference_list)
    lowest = min(difference_list)


newaverage = "{:.2f}".format(theaverage)
new_month = str(new_month)
total_gainloss = str(total_gainloss)
newaverage = str(newaverage)
highest = str(highest)
lowest = str(lowest)

# # time to print results to match view needed
print("Financial Analysis")
print("--------------------------------------------")
print("Total Months: "+ new_month)
print("Total: $"+total_gainloss)
print("Average Change: $"+ newaverage)
print("Greatest Increase in Profits: $"+ highest)
print("Greatest Decrease in Profits: $"+ lowest)

# export of the file
output = open("results.txt","w+")

output.write("Financial Analysis ")
output.write("\n -------------------------------------------- ")
output.write("\nTotal Months: "+ new_month)
output.write("\nTotal: $"+ total_gainloss)
output.write("\nAverage Change: $"+ newaverage)
output.write("\nGreatest Increase in Profits: $"+ highest)
output.write("\nGreatest Decrease in Profits: $"+ lowest)




