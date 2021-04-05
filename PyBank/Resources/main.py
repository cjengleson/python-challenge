#import os and csv
import os

import csv

#create path to csv
pybank_csvpath = os.path.join("..", "Resources", "budget_data.csv")

# set variables
total_months = []
net_profit = []
profit_change = []

# reading through budget data as csvreader
with open(pybank_csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None) # skip header row
    
    # read through each row of data
    for row in csvreader:
        total_months.append(row[0])
        net_profit.append(int(row[1]))
        
        
#print statements
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Net Profit: ${sum(net_profit)}")
    
