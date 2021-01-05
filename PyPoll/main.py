import os
import csv

# Store the file path associated with the PyPoll Challenge
file = os.path.join('Resources', 'election_data.csv')

#Open the file and store the contents in the variable csv
with open(file) as csvfile:
    #CSV reader specifies delimeter and variable that holds content
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Read the first header row first
    csb_header = next(csvreader)

    #loop through each row of data after the hearder
    for row in csvreader: 

        #Sum of rows to find total votes
        total_votes = sum(1 for row in csvreader)



        print("Election Results")
        print("----------------------------")
        print(f"Total Votes: {total_votes}")
#        print("----------------------------")
#        print(f"{winner}: {percent} {tally}")
#        print(f"{secont}: {percent} {tally}")
#        print(f"{third}: {percent} {tally}")
#        print(f"{forth}: {percent} {tally}")
#        print("----------------------------")
#        print(f"Winner: {winner}")
#        print("----------------------------")




