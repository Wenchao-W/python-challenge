# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("election_data.csv")

#   * The total number of votes cast
#   * A complete list of candidates who received votes
#   * The percentage of votes each candidate won
#   * The total number of votes each candidate won
#   * The winner of the election based on popular vote.

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------

TolVote=0
KhanVote=0
CorreyVote=0
LiVote=0
# Open the CSV 
with open(csvpath, newline="", encoding="utf8") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")
    # Loop 
    for row in csvreader:
        TolVote+=1
                         
        if row['Candidate']=="Khan":
            KhanVote+=1
        if row['Candidate']=="Correy":
            CorreyVote+=1
        if row['Candidate']=="Li":
            LiVote+=1
    
KPercent="{0:.3%}".format(KhanVote/TolVote)
CPercent="{0:.3%}".format(CorreyVote/TolVote)
LPercent="{0:.3%}".format(LiVote/TolVote)

output=f"Election Results\n----------------------------\nTotal Votes: {TolVote}\n----------------------------\nKhan:{KPercent} ({KhanVote})\nCorrey:{CPercent} ({CorreyVote})\nLi:{LPercent} ({LiVote})\n"
print(output)
with open("Output.txt", "w") as text_file:
    text_file.write(output)