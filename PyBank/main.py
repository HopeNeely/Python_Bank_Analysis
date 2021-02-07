import os
import csv

# Store the file path associated with the PyBank Challenge
file = os.path.join('Resources', 'budget_data.csv')

#Create empty lists to hold calucaltion
profitloss = []

date = []

#Set the starting value for counting total_months: 
total_months = 0

#Open the file and store the contents in the variable csv
with open(file) as csvfile:
    #CSV reader specifies delimerter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ",") 

    #Read the header row first
    csv_header = next(csvreader)  
    #print(f"CSV Header:{csv_header}")


    #loop each row of data after the header
    for row in csvreader:  
        # add dates to empty dates list as we iterate
        date.append(row[0])

        #Count rows as we iterate to find total_rows
        total_months += 1

        #Add values from row[1] to profitloss list
        value = int(row[1])
        profitloss.append(value)

        #Find the sum of profitloss list and add in the first row that is missing
        total_profitloss = sum(profitloss)
            
    # Calculate the monthly change in profit/loss        
    monthly_change = [profitloss[i + 1] - profitloss[i] for i in range(len(profitloss)-1)]
      
    #Find average change in profit loss
    average_change = sum(monthly_change) / len(monthly_change)

    #Find max change in profits
    max_change = max(monthly_change)
    #print(max_change)

    # Find min change in profits
    min_change = min(monthly_change)
    
    
# pull the date of max change and date of min change
# start by zip-ing my lists         
new_profitloss_csv = zip(date, profitloss, monthly_change)

# Set variable for output file
output_file = os.path.join('analysis', 'new_budget_data.csv')

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Date", "Profit/Loss", "Change in Profit/Loss"])

    # Write in zipped rows
    writer.writerows(new_profitloss_csv)

found = False

#Open the output file to find max and min profit/loss dates
with open(output_file) as csvfile:
    #CSV reader specifies delimerter and variable that holds contents
    csvreader1 = csv.reader(csvfile, delimiter = ",") 

    #Read the header row first
    output_header = next(csvreader1) 
    #print(output_header)  

 
     #loop each row of data after the header looking for min and max to find date
    for row in csvreader1:  
        if row[2] == max_change:
            print(str(row[0]))

            found = True
            break


        














print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {total_profitloss}")
print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profits: max_date {max_change}")
print(f"Greatest Decrease in Profits: min_date {min_change}")
