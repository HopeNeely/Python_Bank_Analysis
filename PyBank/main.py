import os
import csv

# Store the file path associated with the PyBank Challenge
file = os.path.join('Resources', 'budget_data.csv')

#Create empty lists to hold calucaltions
profitloss = []

net_change = []

#Set the starting value for counting total_months: 
# using 1 instead of 0 accounts for starting the count after first_row
total_months = 1

#Open the file store the contents in the variable csv
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

        #Adding to profitloss list
        value = int(row[1])
        profitloss.append(value)
        

        net_change.append(net_change)

        #Find sum of values in row[1] to find total profit
        #create a list to hold profitloss
        #profitloss = []
        #for row in data:
        #    value = int(row[1])
        #    profitloss.append(value)

       #Find profit change from month to month
       #change = []
       #for value in profitloss:


       
           


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
print(f"Total: {sum(profitloss)}")
        #print(f"Average Change: {average(change)}")
        #print(f"Greatest Increase in Profits: {max_date} {max_profit}")
        #print(f"Greatest Decrease in Profits: {min_date} {min_profit}")