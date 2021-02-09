import os
import csv

# Store the file path associated with the PyPoll Challenge
file = os.path.join('Resources', 'election_data.csv')

# Set the starting value for my vote counts
total_votes = 0

khan_votes = 0

correy_votes = 0

li_votes = 0

otooley_votes = 0


# Creade Variable to hold list of candidates who recieved votes
candidates = []



# Open the file using CSV module
with open(file) as csvfile:
    
    # CSV reader specifies delimeter and variable that holds content
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Read the first header row first
    csv_header = next(csvreader)
    #print(csv_header)

    # loop through each row of data after the header
    for row in csvreader:  
        # Count rows as we iterate to find total_votes
        total_votes += 1

        # Find unique names for canditates in row[2] 
        if row[2] not in candidates:
            candidates.append(row[2])
    

        # Count each candidates vote   ### It would be nice have write a function for this. 
        if row[2] == 'Khan':
            khan_votes += 1

        if row[2] == 'Correy':
            correy_votes += 1

        if row[2] == 'Li':
            li_votes += 1        
        
        if row[2] == "O'Tooley":
            otooley_votes += 1


# Calulate the percentage of votes    ### It would be nice to write a funtion for this.
khan_percent = khan_votes / total_votes * 100

correy_percent = correy_votes / total_votes * 100

li_percent = li_votes / total_votes * 100

otooley_percent = otooley_votes / total_votes * 100
        
        
        
# I need to find a way to rank the candidates by vote count. I know max and min... I'm not sure about second and third!
        
        
        #Create dictionary using the built-in function
        #poll = dict()

        #A dictionary of the poll
        #poll = {
        #    "Voter ID": row[0], 
        #    "County": row[1],
        #    "Candidate": row[2]
        #}


        

        #Use dictionarys to hold each candidate's votes

#print(candidates)


# Print out results to terminal
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print("----------------------------")
#print(f"Winner: {winner}")
print("----------------------------")