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