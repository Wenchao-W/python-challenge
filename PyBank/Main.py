# Modules
import os
import csv

# Set path for file. Put the data in the same folder. 
csvpath = os.path.join("budget_data.csv")

# Goal of this homework
# The total number of months included in the dataset
# The total net amount of "Profit/Losses" over the entire period
# The average change in "Profit/Losses" between months over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

# Define initial values for further cal
month=0
totalnet=0
MaxP=0
MaxL=0
# Open the CSV
with open(csvpath, newline="", encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Pop out the header 
    next(csvreader)
    # Loop 
    for i, row in enumerate(csvreader):
        # Cal the total month
        month+=1
        # Cal the total profit/loss
        totalnet+=float(row[1])
        # Find the max profit and record the date                
        if float(row[1])>MaxP:
            MaxP=float(row[1])
            MaxPDate=row[0]
        # Find the max loss and record the date     
        if float(row[1])<MaxL:
            MaxL=float(row[1])
            MaxLDate=row[0]
        # The below is a relatively easy way for this dataset to get the first and last month's proft/loss 
        # in order to cal the average profit/loss between month
        # if row[0]=="Jan-2010":
        #         Start=float(row[1])
        # if row[0]=="Feb-2017":
        #         End=float(row[1])
        # However, the above method requires to review the dataset.
        # The i and enumerate are introduced in the below method 
        if i==0:
            Start=float(row[1])
        if i==month-1:
            End=float(row[1])
# Cal the "Profit/Losses" between months    
AvgPL=(End-Start)/(month-1)

# Print the output in the terminal
output=f"Financial Analysis\n----------------------------\nTotal Months: {month}\nTotal: ${totalnet}\nAverage  Change: ${AvgPL:.2f}\nGreatest Increase in Profits: {MaxPDate} (${MaxP})\nGreatest Decrease in Profits: {MaxLDate} (${MaxL})"
print(output)

# Write a txt file with output in the same folder
with open("Output.txt", "w") as text_file:
    text_file.write(output)
