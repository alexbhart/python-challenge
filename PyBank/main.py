import os
import csv
import math

# bring in csv into script

csvpath = os.path.join('D:\edx_bootcamp\python-challenge\PyBank','Resources','budget_data.csv')

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

    #average_change = total / (len(date))
    #print(average_change)

    pnl_change = [] #creates list that acts as 'third' column of csv 
    for x in pnl: 
        next_row = row
        change = int(sum(row[x]))

# find max 

# find min

# print analysis to terminal

print("Financial Analysis")
print("----------------------------------------------")
print("Total Months: " + str(len(date)))
print(f"Total: ${total}")




#write analysis to new text file

