# Modules
import os
import csv
import us_state_abbrev as us
# Set path for file. Put the data in the same folder. 
csvpath = os.path.join("employee_data.csv")
outpath = os.path.join("employee_data_updated.csv")
# Goal of this project
#   * The `Name` column should be split into separate `First Name` and `Last Name` columns.
#   * The `DOB` data should be re-written into `MM/DD/YYYY` format.
#   * The `SSN` data should be re-written such that the first five numbers are hidden from view.
#   * The `State` data should be re-written as simple two-letter abbreviations.
# Open and write the CSV
with open(csvpath, newline="", encoding="utf8") as csvfile:
    with open(outpath, "w",newline='',encoding="utf8") as outfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        csvwriter = csv.writer(outfile, delimiter=',')
        # Change the header with splited First Name and Last Name
        header=next(csvreader)
        header[1]="First Name"
        header.insert(2,"Last Name")
        # Put the header in the new file
        csvwriter.writerow(header)
        # Loop and input other info into the new csv file
        for row in csvreader:
            # ID
            employ_id=row[0]
            # Name
            name_new=row[1].split()
            # Date
            DateSP=row[2].split("-")
            date_new=f"{DateSP[1]}/{DateSP[2]}/{DateSP[0]}"
            # SSN
            ssnold=row[3].split("-")
            ssn_new=f"xxx-xx-{ssnold[2]}"
            # State
            state_abb=us.us_state_abbrev[row[4]]
            # Write into the file
            csvwriter.writerow([employ_id,name_new[0],name_new[1],date_new,ssn_new,state_abb])         