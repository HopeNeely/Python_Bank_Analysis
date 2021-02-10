# python-challenge
This challenge uses python to analyze two different situations: PyBank and PyPoll. 

PyBank is an analysis of simple financial records of a fictional company.  The financial data given is called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. The goal is to create a Python script that analyzes the records to calculate each of the following:

  * The total number of months included in the dataset
  * The net total amount of "Profit/Losses" over the entire period
  * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
  * The greatest increase in profits (date and amount) over the entire period
  * The greatest decrease in losses (date and amount) over the entire period

The final script is both printed to the terminal and exported a text file with the results.


PyPoll consists of a vote counting process in a fictional small, rural town. The set of poll data given is called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. The goal is to create a Python script that analyzes the votes and calculates each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

Again, the final script is both printed to the terminal and exported a text file with the results.
