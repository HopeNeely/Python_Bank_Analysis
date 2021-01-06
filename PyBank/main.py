import os
import csv

# Store the file path associated with the PyBank Challenge
file = os.path.join('Resources', 'budget_data.csv')

#Open the file store the contents in the variable csv
with open(file) as csvfile:
    #CSV reader specifies delimerter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ",") 

    #Read the header row first
    #csv_header = next(csvreader)  #I commented this out because it was skipping my first line of data
    #print(f"CSV Header:{csv_header}") #No clue why because, I printed the header line just fine. 

    #loop each row of data after the header
    for row in csvreader:  
        #Create list to hold the data from csvreader 
        data = list(csvreader)
        #Length of list will give me total months
        total_months = len(data)   

        #Find sum of values in row[1] to find total profit
        #create a list to hold profitloss
        profitloss = []
        for row in data:
            value = int(row[1])
            profitloss.append(value)

       
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