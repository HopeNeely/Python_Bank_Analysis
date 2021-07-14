import os
import csv

# Store the file path.
file = os.path.join('Resources', 'budget_data.csv')

# Create empty dictionary to hold calculations.
analysis = {
    'profitloss': [],
    'profitloss_with_first_row': [], 
    'date': [],
    'change_in_profitloss': [],
    'change': []
} 

# Create empty lists to hold calculations
# profitloss = []
# profitloss_with_first_row = []
# date = []
# change_in_profitloss = []
# change_list = []

# Set the starting value 1. The first row was null. 
# It was taken out for counting total_months. 
total_months = 1

# # First monthly change is a null value. 
# # We don't know what the value was before our first profit/loss number.
# first_change = ""
# analysis['change_in_profitloss'].append(first_change)

# Open the file and store the contents in the variable csv
with open(file) as csvfile:
    # CSV reader specifies delimerter and variable that holds contents.
    csvreader = csv.reader(csvfile, delimiter = ",") 

    # Read and remove header row.
    csv_header = next(csvreader)  

    # Read the first data row and eliminate from change calculation.
    first_line = next(csvreader)

    # Grab first date to add back to all dates.  
    first_date = first_line[0]
    analysis['date'].append(first_date)

    # Grab first profitloss to add back to all profitloss.
    first_profitloss = int(first_line[1])
    analysis['profitloss_with_first_row'].append(first_profitloss)

    # Loop trough rows after the header and first line.
    for row in csvreader:  
        # add dates to empty dates list as we iterate.
        analysis['date'].append(row[0])

        # Count rows as we iterate to find total_rows.
        total_months += 1

        # Add values to profitloss key.
        value = int(row[1])
        analysis['profitloss'].append(value)
        analysis['profitloss_with_first_row'].append(value)

        # Calculate total profit loss.
        total_profitloss = sum(analysis['profitloss_with_first_row'])
            
    # Calculate the monthly change in profit/loss.      
    for i in range(len(analysis['profitloss_with_first_row'])-1):  
        monthly_change = analysis['profitloss_with_first_row'][i + 1] - analysis['profitloss_with_first_row'][i]
        analysis['change'].append(int(monthly_change))
        # analysis['change_in_profitloss'].append(int(monthly_change))
      
# Find average change in profit loss.
average_change = sum(analysis['change']) / len(analysis['change'])
# print(average_change)

# Find max change in profits.
max_change = max(analysis['change'])
# print(max_change)

# Find min change in profits
min_change = min(analysis['change'])
# print(min_change)
    
# Find the date of max change and date of min change
# # start by zip-ing my lists for the new csv file         
# new_profitloss_csv = zip(date, profitloss_with_first_row, change_in_profitloss)

# # Create output file path.
# output_file = os.path.join('analysis', 'new_budget_data.csv')

# # Open the output file.
# with open(output_file, "w", newline="") as datafile:
#     writer = csv.writer(datafile)

#     # Write the header row
#     writer.writerow(["Date", "Profit/Loss", "Change in Profit/Loss"])

#     # Write in zipped rows
#     writer.writerows(new_profitloss_csv)


# #Open the output file to find max and min profit/loss dates
# with open(output_file) as csvfile:
#     #CSV reader specifies delimerter and variable that holds contents
#     csvreader1 = csv.reader(csvfile, delimiter = ",") 

#     #Read the header row first
#     output_header = next(csvreader1) 
#     #print(output_header)  

# Loop through dictionary looking for min and max to find date
for x in analysis.values(max_change): 
    max_date = analysis['date'][x]
    # elif ['change'] == min_change: 
    #     min_date = ['date']
print(max_date)

# # Text file path in analysis folder
# output_text = os.path.join('analysis', 'budget_analysis.txt')

# #  Open the output file
# with open(output_text, "w") as text_file:

#     text_file.write(f"Financial Analysis \n"
#     "-----------------------------\n"
#     f"Total Months: {total_months}\n"
#     f"Total: ${total_profitloss}\n"
#     f"Average Change: ${average_change:.2f}\n"
#     f"Greatest Increase in Profits: {max_date} (${max_change})\n"
#     f"Greatest Decrease in Profits: {min_date} (${min_change})")

# text_file.close()


# # Print analysis in terminal
# print("Financial Analysis")
# print("-----------------------------")
# print(f"Total Months: {total_months}")
# print(f"Total: ${total_profitloss}")
# print(f"Average Change: ${average_change:.2f}")
# print(f"Greatest Increase in Profits: {max_date} (${max_change})")
# print(f"Greatest Decrease in Profits: {min_date} (${min_change})")
