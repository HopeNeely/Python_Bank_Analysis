# Import Dependencies. 
import os
import csv

# Create variables.
results = {
    'date': [],
    'profitloss': [],
    'change_in_profitloss': []
}

change = []

# First monthly change is a null. Create place holder for that value.
first_change = ""
results['change_in_profitloss'].append(first_change)

# Store file path.
file = os.path.join('Resources', 'budget_data.csv')

# Open file.
with open(file) as csvfile:

    # Read file.
    csvreader = csv.reader(csvfile, delimiter = ",") 

    # Read and remove header row.
    csv_header = next(csvreader)  

    # Loop trough data rows.
    for row in csvreader:  
        # Add dates to empty 'date' key above.
        results['date'].append(row[0])

        # Add values to 'profitloss' key.
        results['profitloss'].append(int(row[1]))

        # Calculate total profit loss.
        total_profitloss = sum(results['profitloss'])
            
    # Calculate the monthly change in profit/loss.      
    for i in range(len(results['profitloss'])-1):  
        monthly_change = results['profitloss'][i + 1] - results['profitloss'][i]
        change.append(int(monthly_change))
        results['change_in_profitloss'].append(int(monthly_change))

# Find total months.
total_months = len(results['date'])

# Find average change in profit loss.
average_change = sum(change) / len(change)

# Find max change in profits.
max_change = max(change)

# Find min change in profits
min_change = min(change)

# Find the date of max change and date of min change
for index, value in enumerate(results['change_in_profitloss']):
    if results['change_in_profitloss'][index] == max_change:
        max_index = index

    elif results['change_in_profitloss'][index] == min_change:
        min_index = index

max_date = results['date'][max_index]

min_date = results['date'][min_index]


# Create text file path in analysis folder
output_text = os.path.join('analysis', 'budget_analysis.txt')

#  Open the output file
with open(output_text, "w") as text_file:
    
    # Write in output file.
    text_file.write(f"Financial Analysis \n"
    "-----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profitloss}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {max_date} (${max_change})\n"
    f"Greatest Decrease in Profits: {min_date} (${min_change})")

text_file.close()


# Print analysis in terminal
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profitloss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_date} (${max_change})")
print(f"Greatest Decrease in Profits: {min_date} (${min_change})")
