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
KhanVote=0
CorreyVote=0
LiVote=0

# Open the CSV 
with open(csvpath, newline="", encoding="utf8") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")
    # Loop 
    for row in csvreader:
        # Cal the total votes
        TolVote+=1
        # Cal the votes for each candidates                 
        if row['Candidate']=="Khan":
            KhanVote+=1
        if row['Candidate']=="Correy":
            CorreyVote+=1
        if row['Candidate']=="Li":
            LiVote+=1
# Cal the percentage of each cadidate    
KPercent="{0:.3%}".format(KhanVote/TolVote)
CPercent="{0:.3%}".format(CorreyVote/TolVote)
LPercent="{0:.3%}".format(LiVote/TolVote)

# Find who is the winner
if KhanVote>CorreyVote and KhanVote>LiVote:
    Winner="Khan"
elif CorreyVote>LiVote:
    Winner="Correy"
else:
    Winner="Li"

# Print the data in terminal
output=f"Election Results\n----------------------------\nTotal Votes: {TolVote}\n----------------------------\nKhan:{KPercent} ({KhanVote})\nCorrey:{CPercent} ({CorreyVote})\nLi:{LPercent} ({LiVote})\n----------------------------\nWinner is {Winner}\n"
print(output)

# Write the text file in the same folder of the output
with open("Output.txt", "w") as text_file:
    text_file.write(output)
