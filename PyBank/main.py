import os
import csv

# Store the file path associated with the PyBank Challenge
file = os.path.join('Resources', 'budget_data.csv')

#Open the file in "read" mode ('r') and store the contents in the variable csv
with open(file) as csvfile:
    #CSV reader specifies delimerter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ",") 

    #Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header:{csv_header}")

    #Read each row of data after the header
    for row in csvreader:
        print(row)

    #Look for greatest increase in profits. Then print with date and amount.
    # for row in csvreader: 
    #     if row[0] == max.SOMETHING...that is the : greatest_change 
    #           print(f'Greatest Increase in Profits: {row[0]} {row[1] )   