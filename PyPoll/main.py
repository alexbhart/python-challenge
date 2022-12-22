import os
import csv
import pandas as pd

#import csv

election_csv = os.path.join("Resources/election_data.csv")
text_results = os.path.join("Analysis/election_analysis.txt")

#read csv

with open(election_csv, 'r') as election_data:

#split the data by commas
    election_results = csv.reader(election_data, delimiter=',')


#determine header columns
    header = next(election_results)
#determine variables for row data for easier recall    
    Ballot_ID = []
    County = []
    Candidate = []
    for row in election_results:
        Ballot_ID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])

   
#cast total number of votes (use len function) to variable for printing later
    total_votes = len(Ballot_ID)
        
 #add unique candidate names to list
    unique_candidates = list(set(Candidate))
    
    

#count individual total of votes
    first_candidate = 0 
    second_candidate = 0
    third_candidate = 0 
    for row in Candidate:
       
        if row == unique_candidates[0]:
            first_candidate += 1 
        elif row == unique_candidates[1]:
            second_candidate += 1
        else: 
            third_candidate += 1    
    
# calculate percentages of total votess
    first_candidate_percentage = round(first_candidate / total_votes * 100, 2)
    second_candidate_percentage = round(second_candidate / total_votes * 100, 2)
    third_candidate_percentage = round(third_candidate / total_votes * 100, 2)        
#winner of the election based on popular vote


dict_results = {
    "Candidate": [unique_candidates],
    "Percentage": [first_candidate_percentage, second_candidate_percentage, third_candidate_percentage],
    "Total Votes": [first_candidate, second_candidate, third_candidate]

}


# Election Results

# ---------------------------------------

# Candidate 1 : Percentage (Total Votes) 
# Candidate 2: Percentage (Total Votes)
# Candidate 3: Percentage (Total Votes)

# ----------------------------------------

# Winner: Max of popular votes

# ---------------------------------------

print("Election Results")
print("---------------------------------")
print(f"{unique_candidates[0]} : {first_candidate_percentage}% ({first_candidate})")
print(f"{unique_candidates[1]} : {second_candidate_percentage}% ({second_candidate})")
print(f"{unique_candidates[2]} : {third_candidate_percentage}% ({third_candidate})")
print("---------------------------------")
print(f"Winner: {dict_results["Candidate"]}!")
print("---------------------------------")

