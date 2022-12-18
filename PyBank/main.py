import os
import csv
import math

# bring in csv into script

csvpath = os.path.join('D:\\edx_bootcamp\\python-challenge\\PyBank','Resources','budget_data.csv')

# establish lists
date = []
pnl = []


# read file

with open(csvpath, "r") as csvfile:
    budget = csv.reader(csvfile, delimiter=',')

# find header rows
    csvheader = next(budget)
    

# get total count of list items in first column
    for row in budget:
        date.append(row[0])
        pnl.append(row[1])

 
       

    
# absolute value of all changes
    
    f_pnl = [float(x) for x in pnl]
    total = int(sum(f_pnl))
   

# average change (sum of changes / number of items)

    

    pnl_change = [] #creates list that acts as 'third' column of csv 
    i_pnl = [int(x) for x in pnl]
    for x in range(len(i_pnl)): 
        if i_pnl[0] == 0:
            change = 0
        else: change = (i_pnl[x-1] + i_pnl[x])
        pnl_change.append(change)
        avg_change = int(sum(pnl_change)) / (len(pnl_change))

# find max 
    maxchange = max(pnl_change)

# find min
    minchange = min(pnl_change)
# print analysis to terminal

print("Financial Analysis")
print("----------------------------------------------")
print("Total Months: " + str(len(date)))
print(f"Total: ${total}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {maxchange}")
print(f"Greatest Decrease in Profits: {minchange}")





#write analysis to new text file

