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