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

candidate_votes = []

candidate_percent = []


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


#print(candidates)

# Append candidate vote count to candidate_vote list
candidate_votes.append(khan_votes)
candidate_votes.append(correy_votes)
candidate_votes.append(li_votes)
candidate_votes.append(otooley_votes)
#print(candidate_votes)

# Calulate the percentage of votes    
khan_percent = khan_votes / total_votes * 100
correy_percent = correy_votes / total_votes * 100
li_percent = li_votes / total_votes * 100
otooley_percent = otooley_votes / total_votes * 100
        
# Append candidate percentatages to candidate percent list
candidate_percent.append(khan_percent)
candidate_percent.append(correy_percent)
candidate_percent.append(li_percent)
candidate_percent.append(otooley_percent)
#print(candidate_percent)

# zip poll results         
poll = zip(candidates, candidate_votes, candidate_percent)

# save the output csv file path
output_csv = os.path.join('analysis', 'poll.csv')

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_csv, "w", newline='') as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Candidate", "Votes Won", "Percentage"])

    writer.writerows(poll)

#Open the output file to find max and min profit/loss dates
with open(output_csv) as csvfile:
    #CSV reader specifies delimerter and variable that holds contents
    csvreader1 = csv.reader(csvfile, delimiter = ",") 

    #Read the header row first
    output_header = next(csvreader1) 
    #print(output_header)  

    # loop each row of data after the header looking for min and max to find date
    for row in csvreader1: 
        if row[1] == str(max(candidate_votes)): 
            winner = row[0]
            winner_vote = row[1]
            winner_percent = float(row[2])

# Write text file with analysis
output_text = os.path.join('analysis', 'poll_analysis.txt')

#  Open the output file
with open(output_text, "w") as text_file:

    text_file.write("Election Results \n"
    "---------------------------- \n"
    f"Total Votes: {total_votes} \n"
    "----------------------------\n"
    f"{winner}: {winner_percent:.3f}% ({winner_vote})\n"
    f"Correy: {correy_percent:.3f}% ({correy_votes})\n"
    f"Li: {li_percent:.3f}% ({li_votes})\n"
    f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})\n"
    "----------------------------\n"
    f"Winner: {winner}\n"
    "----------------------------\n"
text_file.close()

# Print out results to terminal
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
print(f"{winner}: {winner_percent:.3f}% ({winner_vote})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")