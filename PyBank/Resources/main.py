#import os and csv
import os

import csv

#create path to csv
pybank_csvpath = os.path.join("..", "Resources", "budget_data.csv")

# set variables
total_months = []
net_profit = []
monthly_profit_change = []
overall_profit_change = 0

# reading through budget data as csvreader
with open(pybank_csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None) # skip header row
    
    # read through each row of data
    for row in csvreader:
        total_months.append(row[0])
        net_profit.append(int(row[1]))
    
    for i in range(len(net_profit)-1):
        # make a new list where following month (ie Feb 2010) - current month (ie January 2010)
        # to find the monthly profit change
        monthly_profit_change.append(net_profit[i+1]-net_profit[i])

        # find average profit change
        overall_profit_change = int(sum(monthly_profit_change)) / int(len(monthly_profit_change))

        # format accordingly using 2 decimal places
        formatted_profit_change = "{:.2f}".format(overall_profit_change)


# find maximum/minimum monthly profit change        
max_increase = max(monthly_profit_change)
min_increase = min(monthly_profit_change)

# associate month with monthly profit change using index function to find month where
# profit change happened, + 1 to change month output to the next month
max_month = monthly_profit_change.index(max_increase) + 1
min_month = monthly_profit_change.index(min_increase) + 1

# set total net profit
net_profit = int(sum(net_profit))

print("----------------------------")
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(len(total_months)))
print("Total: " + str(net_profit))
print("Average Change: " + str(formatted_profit_change))
print(f"Greatest Increase in Profits: {total_months[max_month]} (${str(max_increase)})")  
print(f"Greatest Decrease in Profits: {total_months[min_month]} (${str(min_increase)})")

# export to text file
output_txt_file = open("../analysis/Budget_Analysis.txt", "w")
output_txt_file.write("Financial Analysis")
output_txt_file.write("\n")
output_txt_file.write("----------------------------")
output_txt_file.write("\n")
output_txt_file.write("Total Months: " + str(len(total_months)))
output_txt_file.write("\n")
output_txt_file.write("Total: " + str(net_profit))
output_txt_file.write("\n")
output_txt_file.write("Average Change: " + str(formatted_profit_change))
output_txt_file.write("\n")
output_txt_file.write(f"Greatest Increase in Profits: {(total_months[max_month])} (${str(max_increase)})")  
output_txt_file.write("\n")
output_txt_file.write(f"Greatest Decrease in Profits: {(total_months[min_month])} (${str(min_increase)})")