# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("budget_data.csv")

# The total number of months included in the dataset

# The total net amount of "Profit/Losses" over the entire period

# The average change in "Profit/Losses" between months over the entire period

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period

month=0
totalnet=0
AvgPL=0
MaxP=0
MaxPDate=[]
MaxL=0
MaxLDate=[]
# Open the CSV
with open(csvpath, newline="", encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    next(csvreader)
    
    # Loop 
    for row in csvreader:
        month+=1
        totalnet+=float(row[1])
       
        # if row[0]=="Jan-2010":
        #         Start=float(row[1])
        # if row[0]=="Feb-2017":
        #         End=float(row[1])
                
        if float(row[1])>MaxP:
            MaxP=float(row[1])
            MaxPDate=row[0]
        if float(row[1])<MaxL:
            MaxL=float(row[1])
            MaxLDate=row[0]

with open(csvpath, newline="", encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    next(csvreader)
    for i, row in enumerate(csvreader):
        if i==0:
            Start=float(row[1])
        if i==month-1:
            End=float(row[1])
    
AvgPL=(End-Start)/(month-1)

output=f"Financial Analysis\n----------------------------\nTotal Months: {month}\nTotal: ${totalnet}\nAverage  Change: ${AvgPL:.2f}\nGreatest Increase in Profits: {MaxPDate} (${MaxP})\nGreatest Decrease in Profits: {MaxLDate} (${MaxL})"
print(output)
with open("Output.txt", "w") as text_file:
    text_file.write(output)
# print(f"Financial Analysis\n----------------------------\nTotal Months: {month}\nTotal: ${totalnet}\nAverage  Change: ${AvgPL:.2f}\nGreatest Increase in Profits: {MaxPDate} (${MaxP})\nGreatest Decrease in Profits: {MaxLDate} (${MaxL})")