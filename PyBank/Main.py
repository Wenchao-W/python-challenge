# Modules
import os
import csv

# Set path for file. Put the data in the same folder. 
csvpath = os.path.join("budget_data.csv")

# Goal of this project
# The total number of months included in the dataset
# The total net amount of "Profit/Losses" over the entire period
# The average change in "Profit/Losses" between months over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

# Define initial values for further calculation
month=0
totalnet=0
Last=0
MaxP=0
MaxL=0
# Open the CSV
with open(csvpath, newline="", encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Pop out the header 
    next(csvreader)
    # Convert the generator to list
    csvreader=list(csvreader)
    # Loop 
    for row in csvreader:
        # Calculate the total month
        month+=1
        # Calculate the total profit/loss
        totalnet+=float(row[1])
        # Calculate the monthly difference
        DiffMonthly=float(row[1])-Last
        # Find the max profit and record the date                
        if DiffMonthly>MaxP:
            MaxP=DiffMonthly
            MaxPDate=row[0]
        # Find the max loss and record the date     
        if DiffMonthly<MaxL:
            MaxL=DiffMonthly
            MaxLDate=row[0]
# Get the last month's "Profit/Losses"
        Last=float(row[1])
# Get the first month's "Profit/Losses" 
Begin = float(csvreader[0][1])
# Calculate the Average "Profit/Losses" between months
AvgPL=(Last-Begin)/(month-1)

# Print the output in the terminal
output=f"Financial Analysis\n----------------------------\nTotal Months: {month}\nTotal: ${totalnet}\nAverage  Change: ${AvgPL:.2f}\nGreatest Increase in Profits: {MaxPDate} (${MaxP})\nGreatest Decrease in Profits: {MaxLDate} (${MaxL})"
print(output)

# Write a txt file with output in the same folder
with open("Output.txt", "w") as text_file:
    text_file.write(output)
