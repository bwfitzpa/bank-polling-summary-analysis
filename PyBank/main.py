#PyBank
#Importing CSV file
import os
import csv
budget_data = os.path.join('..', 'Resources','budget_data.csv')
total = 0
increase = 0
decrease = 0
profit_losses_list = []
date_list = []
#opening the CSV file, to do this I modified the code from the "ReadCSV" in class example
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    #giving the header
    csv_header = next(csv_file)
    #finding the sum of profits/losses, I looked up the "+=" to add to a list using Stack Overflow
    for row in csv_reader:
        profit_losses = int(row[1])
        total += profit_losses
    #putting profit_losses into a list
        profit_losses_list.append(profit_losses)
    #putting date into a list
        date = str(row[0])
        date_list.append(date)
total_months = len(date_list)
#creating a function to find increase/decrease month to month
all_change= []
def change(month):
    differences = []
    for i in range(1, len(month)):
        difference = month[i] - month[i-1]
        differences.append(difference)
    return differences
all_change = (change(profit_losses_list))
#finding the greatest increase
greatest_increase = max(all_change)
#finding the greatest decrease
greatest_decrease = min(all_change)
average_change = sum(all_change)/len(all_change)
#adding a space at the front of the profit/losses change list to make the same length as the date list
space = [' ']
all_change = space + all_change
#finding the date of the greatest increase
greatest_increase_index = all_change.index(greatest_increase)
greatest_increase_date = date_list[greatest_increase_index]
#finding the date of the greatest decrease
greatest_decrease_index = all_change.index(greatest_decrease)
greatest_decrease_date = date_list[greatest_decrease_index]
#printing out the results
print("Financial Analysis")
print("----------------------------------")
print("Total Months:" + str(total_months))
print("Total: $" + str(total))
#formatting average change to be two decimal points, looked on python.com to find how to format to number of decimal points
average_change_hundreds = "{:.2f}".format(average_change)
print("Average Change:" + str(average_change_hundreds))
print("Greatest Increase in Profits: " + str(greatest_increase_date) + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + str(greatest_decrease_date) + " ($" + str(greatest_decrease) + ")")
#printing the output to the analysis.txt file, looked up how to print to a .txt file and add spaces on Stack Overflow
file_path = os.path.join('..', 'analysis','analysis.txt')
with open(file_path, 'a') as text:
    text.write("_______________________________________________________\n" + "\n")
    text.write("Financial Analysis\n" + "\n")
    text.write("----------------------------------\n" + "\n")
    text.write("Total Months:" + str(total_months) + "\n" + "\n")
    text.write("Total: $" + str(total) + "\n" + "\n")
    text.write("Average Change:" + str(average_change_hundreds) + "\n" + "\n")
    text.write("Greatest Increase in Profits: " + str(greatest_increase_date) + " ($" + str(greatest_increase) + ")" + "\n" + "\n")
    text.write("Greatest Decrease in Profits: " + str(greatest_decrease_date) + " ($" + str(greatest_decrease) + ")" + "\n" + "\n")

###########################################################################################################################
print("_______________________________________________________")
#PyPoll
#PyBank
#Importing CSV file
import os
import csv
election_data = os.path.join('..', 'Resources','election_data.csv')
#create empty variables
ballot_id = []
county = []
candidate = []
#opening the CSV file, to do this I modified the code from the "ReadCSV" in class example
with open(election_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    #adding the data from the CSV file to the candidate list
    for row in csv_reader:
        candidate_row = str(row[2])
        candidate.append(candidate_row)
#finding the total number of votes cast
print("Election Results")
print("----------------------------------")
total_votes = len(candidate)
print("Total Votes: " + str(total_votes))
print("----------------------------------")
#creating a list of the unique candidates called candidate_list, looked up on python.org how to create a list of unique elements from a list
candidates = set(candidate)
candidate_list = list(candidates)
#counting the number of votes for each candidate, creating a dictionary to hold this, also looked up the count function on python.org
votes_per_candidate = {}
for value in candidate_list:
    candidate_votes = candidate.count(value)
    votes_per_candidate[value] = candidate_votes
#creating a list of votes, found the .values command on Stack OverFlow
candidate_votes = []
candidate_votes = list(votes_per_candidate.values())
candidate_votes1 = candidate_votes
#finding the percentages
vote_percentage = []
for candidate_votes1 in candidate_votes1:
    vote_percent = (candidate_votes1/total_votes) * 100
    vote_percentage.append(vote_percent)
#changing the list to be to the hundreds
#formatting average change to three decimal points, looked on python.com to find how to format to number of decimal points
vote_percentage_thousands = ["{:.3f}".format(vote_percentage) for vote_percentage in vote_percentage]
#printing out the results by candidate, modified the code from the "list_comprehensions" in-class exercise
for candidate, percentage, votes in zip(candidate_list, vote_percentage_thousands, candidate_votes):
    print(f"{candidate}: {percentage}% ({votes})")
print("----------------------------------")
#finding the winner of the election
most_votes = max(candidate_votes)
most_votes_index = candidate_votes.index(most_votes)
most_votes_candidate = candidate_list[most_votes_index]
print("Winner: " + str(most_votes_candidate))
print("----------------------------------")
#adding these results to the analysis.txt file
#printing the output to a text file, looked up how to print to a .txt file and add spaces on Stack Overflow
file_path = os.path.join('..', 'analysis','analysis.txt')
with open(file_path, 'a') as text:
    text.write("_______________________________________________________\n" + "\n")
    text.write("Election Results\n" + "\n")
    text.write("----------------------------------\n" + "\n")
    text.write("Total Votes: " + str(total_votes) + "\n" + "\n")
    text.write("----------------------------------\n" + "\n")
    for candidate, percentage, votes in zip(candidate_list, vote_percentage_thousands, candidate_votes):
        text.write(f"{candidate}: {percentage}% ({votes})\n"+ "\n")
    text.write("----------------------------------\n" + "\n")
    text.write("Winner: " + str(most_votes_candidate) + "\n" + "\n")
    text.write("----------------------------------\n" + "\n")