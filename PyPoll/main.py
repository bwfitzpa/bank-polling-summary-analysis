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
#opening the file
with open(election_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    ####print(csv_header)
    #creating variables for Ballot ID, County, Candidate
    for row in csv_reader:
        ballot_id_row = int(row[0])
        ballot_id.append(ballot_id_row)
        county_row = str(row[1])
        county.append(county_row)
        candidate_row = str(row[2])
        candidate.append(candidate_row)
# check/clean the data
print(ballot_id)
candidate_unique = list(set(candidate))
print(candidate_unique)
