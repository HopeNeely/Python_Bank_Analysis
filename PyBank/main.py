import os
import csv

# Store the file path associated with the PyBank Challenge
file = os.path.join('Resources', 'budget_data.csv')

#Create empty lists to hold calucaltion
profitloss = []

net_change = []

#Set the starting value for counting total_months: 
# using 1 instead of 0 accounts for starting the count after first_row
total_months = 1

#Open the file and store the contents in the variable csv
with open(file) as csvfile:
    #CSV reader specifies delimerter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ",") 

    #Read the header row first
    csv_header = next(csvreader)  
    #print(f"CSV Header:{csv_header}")
    
    #Read the first row of data
    first_row = next(csvreader)
    #print(first_row)

    older_value = int(first_row[1])

    #loop each row of data after the header
    for row in csvreader:  
        #Count rows as we iterate to find total_rows
        total_months += 1

        #Add values from row[1] to profitloss list
        value = int(row[1])
        profitloss.append(value)
        
        #Find the sum of profitloss list and add in the first row that is missing
        total_profitloss = sum(profitloss) + older_value
        
        #Find change in profitloss month to month
        #Put values from profitlos and first row into list
        ##profitloss_with_first_row = [older_value] + profitloss

        ##monthly_change = profitloss_with_first_row - profitloss 
        ##net_change.append(monthly_change)
        #print(net_change)
      
        #Find average change in profit loss
        ##average_change = sum(net_change) / len(net_change)
        
           


#
 #           print(change)
        #Write a function that returns the arithmetic average
        #def average(numbers):
        #    length = len(numbers)
        #    total = 0.0
        #    for number in numbers:
        #        total += number
        #    return total / length

        

    #Look for greatest increase in profits. Then print with date and amount.
    # for row in csvreader: 
    #     if row[0] == max.SOMETHING...that is the : greatest_change 
    #           print(f'Greatest Increase in Profits: {row[0]} {row[1] )   

print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {total_profitloss}")
##print(f"Average Change: {average_change}")
        #print(f"Greatest Increase in Profits: {max_date} {max_profit}")
        #print(f"Greatest Decrease in Profits: {min_date} {min_profit}")