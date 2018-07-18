# Import the necessary libraries so that Python is able to interpret properly
import os
import csv
import math

# Now we need to join the filepaths to make the csv file accessible 
csvpath = os.path.join(".", "Resources", "budget_data.csv")

# Create an empty list containing the months, we will use this to calculate the total months and then average
month = []
# Create an empty list containing the monthly revenue
revenue = []

# Now we will open the filepath as a csv file
# newline = "" designates where new lines will start...  The file is defaulted as read-only
with open(csvpath, newline="") as BankFile:

    csvreader = csv.reader(BankFile, delimiter=",")
    
    # Loop through the first column in the csv-file
    # row[0] should correspond to the 1st index (row A)

    for row in csvreader:
        # Add to the month list
        month.append(row[0])
    
    
        revenue.append(row[1])
           
# Output Format
print('Financial Analysis')
print('-----------------------------------------')

# 1. The total number of months in the data set is the entirety of column 1 within the excel file, -1, to account for header cell
totalMonths = len(month) - 1
print(f'The total number of months in our dataset is {str(totalMonths)}.')

# Needed to exclude the first row (Column Header) from our revenue list
newRevenue = (revenue[1: len(revenue)])
# Need to convert all of the values within our list to integers
newRevenue = [int(i) for i in newRevenue]
# 2. Need to sum all of our integers within our revenue list
totalRevenue = sum(newRevenue)
print(f'The total revenue at this bank was ${totalRevenue}.')

# Average change is not just total revenue/total months...  We want an average of the change, month to month.  Create new list to find month-to-month
# revenue change
revenueChange = []

for i in range(1, len(newRevenue)):
    revenueChange.append(newRevenue[i] - newRevenue[i-1])

# 3. Need to find the average monthly change in revenue
avgChange = sum(revenueChange)/len(revenueChange)
print(f"Avereage Change: ${round(avgChange, 2)}")

# 4a. Need to find the maximum revenue change, can use the "max" function to operate on the list 
maxRevenueChange = max(revenueChange)
# 4b. Also need to find what date the maximum change occurred on.  Use the index location of the max change to also interrogate the month list.
maxRevenueChangeDate = str(month[revenueChange.index(max(revenueChange))])
print(f"Greatest Increase in Profits: {maxRevenueChangeDate} ($ {maxRevenueChange})")

# 5a. Need to find the minimum change in revenue using the "min" function
minRevenueChange = min(revenueChange)
# 5b. Find the minimum change date
minRevenueChangeDate = str(month[revenueChange.index(min(revenueChange))])
print(f"Greatest Decrease in Revenue: {minRevenueChangeDate} ($ {minRevenueChange})")

# 6. Need to export this message as a text-file
# I've tried to get the lines to be printed on separate lines, but haven't had any success.  Tried appending, opening as 'a' file, ending new lines with '\n', etc.
outputFile = open('./Output.text', 'w', newline='')
outputFile.write('Financial Analysis')
outputFile.write('------------------------------')
outputFile.write(f'The total number of months in our dataset is {str(totalMonths)}.')
outputFile.write(f'The total revenue at this bank was ${totalRevenue}.')
outputFile.write(f'Avereage Change: ${round(avgChange, 2)}')
outputFile.write(f'Greatest Increase in Profits: {maxRevenueChangeDate} ($ {maxRevenueChange})')
outputFile.close()
