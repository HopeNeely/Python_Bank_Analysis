import os
import csv

# Store the file path associated with the PyPoll Challenge
file = os.path.join('Resources', 'election_data.csv')

#Open the file using CSV module
with open(file) as csvfile:
    
    #CSV reader specifies delimeter and variable that holds content
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Read the first header row first
    csv_header = next(csvreader)
    print(csv_header)

    #loop through each row of data after the hearder
    for row in csvreader: 

        #Create dictionary to hold csvreader info
        #poll = {}

        #Create dictionary using the built-in function
        #poll = dict()

        #A dictionary of the poll
        #poll = {
        #    "Voter ID": row[0], 
        #    "County": row[1],
        #    "Candidate": row[2]
        #}

        votes = [row[2]]

        print(len(votes))
        #print(total_votes)

        #Sum of rows to find total votes (SHOULD THIS BE A LIST???)
        

        #Use dictionarys to hold each candidate's votes


        #Print out results
        #print("Election Results")
        #print("----------------------------")
        #print(f"Total Votes: {total_votes}")
#        print("----------------------------")
#        print(f"{winner}: {percent} {tally}")
#        print(f"{secont}: {percent} {tally}")
#        print(f"{third}: {percent} {tally}")
#        print(f"{forth}: {percent} {tally}")
#        print("----------------------------")
#        print(f"Winner: {winner}")
#        print("----------------------------")