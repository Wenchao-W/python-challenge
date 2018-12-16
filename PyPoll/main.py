# Modules
import os
import csv

# Set path for file. Put the data in the same folder
csvpath = os.path.join("election_data.csv")

#  Project goal
#   * The total number of votes cast
#   * A complete list of candidates who received votes
#   * The percentage of votes each candidate won
#   * The total number of votes each candidate won
#   * The winner of the election based on popular vote.

# Provide the initial value for cal
TolVote=0
candidate_name=[]
votedetails=''

# Open the CSV and convert it to a two level list 
with open(csvpath, newline="", encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    data=list(csvreader)

for i in data:
    # Cal the total votes
    TolVote+=1
    # Find all the candidates                 
    if i[2] not in candidate_name:
        candidate_name.append(i[2])
# Find number of candidate
candidate_number=len(candidate_name)
# Give each candidate an initial zero votes and percentage
candidate_vote=[0]*candidate_number
VotePercent=[0]*candidate_number
# Calculate the votes of each candidate
for i in data:
    for j in range(candidate_number):
        if i[2]==candidate_name[j]:
            candidate_vote[j]+=1
# Calculate the percentage of vote for each candidate and record the voting details
for i in range(candidate_number):
    VotePercent[i]="{0:.3%}".format(candidate_vote[i]/TolVote)
    votedetails+=(f'{candidate_name[i]}: {VotePercent[i]} ({candidate_vote[i]})\n')
# Find the winner of the election
winner=candidate_name[candidate_vote.index(max(candidate_vote))]
# Write the election results into an output and print it    
output=f'Election Results\n----------------------------\nTotal Votes: {TolVote}\n----------------------------\n{votedetails}----------------------------\nWinner is {winner}'
print(output)

# Write the text file in the same folder of the output
with open("Output.txt", "w") as text_file:
    text_file.write(output)
