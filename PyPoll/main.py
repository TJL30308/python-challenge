import os 
import csv

with open ('election_data.csv') as file:
    election_data = csv.reader(file) # reads CSV file
    next(election_data, None) # skips header

    candidates = [] # list to store candidates
    vote_count = [] # list to store candidate vote counts
    total_votes = 0 # initiate variable
    vote_percentages = [] # list to store vote percentages
    
    for row in election_data: # loop through election data
        total_votes += 1 # count votes
        candidate = row[2] # select candidate
        vote_percentage = 0 # initiate variable

        if candidate in candidates:
            candidate = candidates.index(candidate) # adds candidate to specific index in candidates list
            vote_count[candidate] = vote_count[candidate] + 1 # adds vote to candidate index in vote_count list
        
        else:
            candidates.append(candidate) # when new candidate add to candidates list
            vote_count.append(1) # adds index to count votes for new candidate
    
    for candidate in range(int(len(candidates))): # loops through candidates list
        vote_percentage = round((vote_count[candidate]) / (total_votes) * 100 , 2) # calculates vote percentage for each candidate
        vote_percentages.append(vote_percentage) # adds vote_percentage to list

    winner = candidates[vote_percentages.index(max(vote_percentages))] # finds max vote percentage index in list then returns the candidate at that index

print("Election Results")
print("---------------------")
print("Total Votes: " + str(total_votes))
print("---------------------")
print(f"{candidates[0]}: {vote_percentages[0]}% ({vote_count[0]})")
print(f"{candidates[1]}: {vote_percentages[1]}% ({vote_count[1]})")
print(f"{candidates[2]}: {vote_percentages[2]}% ({vote_count[2]})")
print(f"{candidates[3]}: {vote_percentages[3]}% ({vote_count[3]})")
print("---------------------")
print(f"Winner: {winner}")
print("---------------------")

pypoll_results = 'pypoll_results.txt'

with open(pypoll_results, 'w') as file_object:
    file_object.write("Election Results\n")
    file_object.write("---------------------\n")
    file_object.write("Total Votes: " + str(total_votes) + "\n")
    file_object.write("---------------------\n")
    file_object.write(f"{candidates[0]}: {vote_percentages[0]}% ({vote_count[0]}) \n")
    file_object.write(f"{candidates[1]}: {vote_percentages[1]}% ({vote_count[1]}) \n")
    file_object.write(f"{candidates[2]}: {vote_percentages[2]}% ({vote_count[2]}) \n")
    file_object.write(f"{candidates[3]}: {vote_percentages[3]}% ({vote_count[3]}) \n")
    file_object.write("--------------------- \n")
    file_object.write(f"Winner: {winner} \n")
    file_object.write("--------------------- \n")
