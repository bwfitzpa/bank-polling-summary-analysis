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
#opening the file
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    #giving the header
    csv_header = next(csv_file)
    #finding the sum of profits/losses, need to say where I got the += from, stack overflow
    for row in csv_reader:
        profit_losses = int(row[1])
        total += profit_losses
    #putting profit_losses into a list
        profit_losses_list.append(profit_losses)
    #putting date into a list
        date = str(row[0])
        date_list.append(date)
total_months = len(date_list)
#breaking up the lists by day of month, need to say where I got how to break by the day of the month
    #creating for the 10th
break1 = 12
ten_pl_list = profit_losses_list[:break1]
ten_date_list = date_list[:break1]
    #creating for the 11th
break2 = (break1 + 12)
eleven_pl_list = profit_losses_list[break1:break2]
eleven_date_list = date_list[break1:break2]
    #creating for the 12th
break3 = (break2 + 12)
twelve_pl_list = profit_losses_list[break2:break3]
twelve_date_list = date_list[break2:break3]
    #creating for the 13th
break4 = (break3 + 12)
thirteen_pl_list = profit_losses_list[break3:break4]
thirteen_date_list = date_list[break3:break4]
    #creating for the 14th
break5 = (break4 + 12)
fourteen_pl_list = profit_losses_list[break4:break5]
fourteen_date_list = date_list[break4:break5]
    #creating for the 15th
break6 = (break5 + 12)
fifteen_pl_list = profit_losses_list[break5:break6]
fifteen_date_list = date_list[break5:break6]
    #creating for the 16th
break7 = (break6 + 12)
sixteen_pl_list = profit_losses_list[break6:break7]
sixteen_date_list = date_list[break6:break7]
    #creating for the 17th
break8 = (break7 + 12)
seventeen_pl_list = profit_losses_list[break7:]
seventeen_date_list = date_list[break7:]
#creating a function to find increase/decrease month to month, need to say where I got this
def change(month):
    differences = []
    for i in range(1, len(month)):
        difference = month[i] - month[i-1]
        differences.append(difference)
    return differences
#running that function and adding the results to a new list to make a new list of all results
ten_change = (change(ten_pl_list))
eleven_change = (change(eleven_pl_list))
twelve_change = (change(twelve_pl_list))
thirteen_change = (change(thirteen_pl_list))
fourteen_change = (change(fourteen_pl_list))
fifteen_change = (change(fifteen_pl_list))
sixteen_change = (change(sixteen_pl_list))
seventeen_change = (change(seventeen_pl_list))
#adding the lists that were just created to one list to find greatest increase and greatest decrease
all_change= []
all_change = ten_change + eleven_change + twelve_change + thirteen_change + fourteen_change + fifteen_change + sixteen_change + seventeen_change
greatest_increase = max(all_change)
greatest_decrease = min(all_change)
average_change = sum(all_change)/len(all_change)
#finding the index in the list for greatest_increase and greatest decrease and then finding the date for each of these
#need to add spaces to the list because change shortens the list
space = [' ']
change_entire_period = []
change_entire_period = space + ten_change + space + eleven_change + space + twelve_change + space + thirteen_change + space + fourteen_change + space + fifteen_change + space + sixteen_change + space + seventeen_change
#finding the date of the greatest increase
greatest_increase_index = change_entire_period.index(greatest_increase)
greatest_increase_date = date_list[greatest_increase_index]
#finding the date of the greatest decrease
greatest_decrease_index = change_entire_period.index(greatest_decrease)
#print(greatest_decrease_index)
greatest_decrease_date = date_list[greatest_decrease_index]
#printing out the results
print("Financial Analysis")
print("----------------------------------")
print("Total Months:" + str(total_months))
print("Total: $" + str(total))
#formatting average change to be two decimal points, put not where I got this command from
average_change_hundreds = "{:.2f}".format(average_change)
print("Average Change:" + str(average_change_hundreds))
print("Greatest Increase in Profits: " + str(greatest_increase_date) + " ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + str(greatest_decrease_date) + " ($" + str(greatest_decrease) + ")")
#printing the output to a text file, need to say where I got the text.write command from, and how to do
#next line with \n (stack overflow)
file_path = os.path.join('..', 'analysis','analysis.txt')
with open(file_path, 'w') as text:
    text.write("Financial Analysis\n" + "\n")
    text.write("----------------------------------\n" + "\n")
    text.write("Total Months:" + str(total_months) + "\n" + "\n")
    text.write("Total: $" + str(total) + "\n" + "\n")
    text.write("Average Change:" + str(average_change_hundreds) + "\n" + "\n")
    text.write("Greatest Increase in Profits: " + str(greatest_increase_date) + " ($" + str(greatest_increase) + ")" + "\n" + "\n")
    text.write("Greatest Decrease in Profits: " + str(greatest_decrease_date) + " ($" + str(greatest_decrease) + ")" + "\n" + "\n")