import os
import csv

# Store the file path.
file = os.path.join('Resources', 'election_data.csv')

# Set the starting value for my vote counts.
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0


# Create dictionary to hold results. 
results = {
    'candidates': [],
    'candidate_votes': [],
    'candidate_percent': []
}

# Open and read file.
with open(file) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Read and remove header row.
    csv_header = next(csvreader)

    # Loop through each row after header.
    for row in csvreader:  
        # Count rows as we iterate to find total_votes
        total_votes += 1

        # Find unique names for candidates in row[2] 
        if row[2] not in results['candidates']:
            results['candidates'].append(row[2])
                   
        # Count each candidates vote. 
        if row[2] == 'Khan':
            khan_votes += 1

        if row[2] == 'Correy':
           correy_votes += 1
        
        if row[2] == 'Li':
            li_votes += 1        

        if row[2] == "O'Tooley":
            otooley_votes += 1


# Append candidate vote count to candidate_votes.
results['candidate_votes'].append(khan_votes)
results['candidate_votes'].append(correy_votes)
results['candidate_votes'].append(li_votes)
results['candidate_votes'].append(otooley_votes)

# Calculate percentages and append to candidate_percent.
for x in results['candidate_votes']:
    percent = x / total_votes * 100
    results['candidate_percent'].append(percent)

# Find winner_vote and name of winner.
winner_vote = max(results['candidate_votes'])

for index, value in enumerate(results['candidate_votes']): 
    if results['candidate_votes'][index] == winner_vote:
        winner_index = index
   
winner = results['candidates'][winner_index]
winner_percent = results['candidate_percent'][winner_index]

second = results['candidates'][1]
second_votes = results['candidate_votes'][1]
second_percent = results['candidate_percent'][1]

third = results['candidates'][2]
third_votes = results['candidate_votes'][2]
third_percent = results['candidate_percent'][2]

forth = results['candidates'][3]
forth_votes = results['candidate_votes'][3]
forth_percent = results['candidate_percent'][3]

# Write text file with analysis
output_text = os.path.join('analysis', 'poll_analysis.txt')

#  Open the output file
with open(output_text, "w") as text_file:

    text_file.write("Election Results \n"
    "---------------------------- \n"
    f"Total Votes: {total_votes} \n"
    "----------------------------\n"
    f"{winner}: {winner_percent:.3f}% ({winner_vote})\n"
    f"{second}: {second_percent:.3f}% ({second_votes})\n"
    f"{third}: {third_percent:.3f}% ({third_votes})\n"
    f"{forth}: {forth_percent:.3f}% ({forth_votes})\n"
    "----------------------------\n"
    f"Winner: {winner}\n"
    "----------------------------\n")
text_file.close()

# Print results in terminal
print("Election Results")
print("----------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------")
print(f"{winner}: {winner_percent:.3f}% ({winner_vote})")
print(f"{second}: {second_percent:.3f}% ({second_votes})")
print(f"{third}: {third_percent:.3f}% ({third_votes})")
print(f"{forth}: {forth_percent:.3f}% ({forth_votes})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")