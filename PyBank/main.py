import os
import csv

# Store the file path associated with the PyBank Challenge
file = os.path.join('Resources', 'budget_data.csv')

#Create empty lists to hold calucaltion
profitloss = []
profitloss_with_first_row = []
date = []
change_in_profitloss = []
change_list = []

#Set the starting value 1 to count the first row that was taken out for counting total_months: 
total_months = 1

#first monthly change is a null value, we don't know what the value was before our first profit/loss number
first_change = ""
change_in_profitloss.append(first_change)

#Open the file and store the contents in the variable csv
with open(file) as csvfile:
    #CSV reader specifies delimerter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ",") 

    #Read the header row first
    csv_header = next(csvreader)  
    #print(f"CSV Header:{csv_header}")

    #Read the first row to eliminate from change calculation
    first_line = next(csvreader)  
    first_date = first_line[0]
    date.append(first_date)
    first_profitloss = int(first_line[1])
    profitloss_with_first_row.append(first_profitloss)
    #print(first_line)

    #loop each row of data after the header and first line
    for row in csvreader:  
        # add dates to empty dates list as we iterate
        date.append(row[0])

        #Count rows as we iterate to find total_rows
        total_months += 1

        #Add values from row[1] to profitloss list
        value = int(row[1])
        profitloss.append(value)
        profitloss_with_first_row.append(value)

        #Find the sum of profitloss list and add in the first row that is missing
        total_profitloss = sum(profitloss_with_first_row)
            
    # Calculate the monthly change in profit/loss      
    for i in range(len(profitloss_with_first_row)-1):  
        monthly_change = profitloss_with_first_row[i + 1] - profitloss_with_first_row[i]
        change_list.append(int(monthly_change))
        change_in_profitloss.append(int(monthly_change))
      
#Find average change in profit loss
average_change = sum(change_list) / len(change_list)

#Find max change in profits
max_change = max(change_list)
#print(max_change)

# Find min change in profits
min_change = min(change_list)
    
    
## Find the date of max change and date of min change
# start by zip-ing my lists for the new csv file         
new_profitloss_csv = zip(date, profitloss_with_first_row, change_in_profitloss)

# Set variable for output file
output_file = os.path.join('analysis', 'new_budget_data.csv')

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Date", "Profit/Loss", "Change in Profit/Loss"])

    # Write in zipped rows
    writer.writerows(new_profitloss_csv)


#Open the output file to find max and min profit/loss dates
with open(output_file) as csvfile:
    #CSV reader specifies delimerter and variable that holds contents
    csvreader1 = csv.reader(csvfile, delimiter = ",") 

    #Read the header row first
    output_header = next(csvreader1) 
    #print(output_header)  

    # loop each row of data after the header looking for min and max to find date
    for row in csvreader1: 
        if row[2] == str(max_change): 
            max_date = row[0]
    

        elif row[2] == str(min_change): 
            min_date = row[0]


# Write text file with analysis
output_text = os.path.join('analysis', 'budget_analysis.txt')

#  Open the output file
with open(output_text, "w") as text_file:

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
