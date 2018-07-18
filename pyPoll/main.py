import os
import csv
import pandas as  pd
import numpy as np
from collections import defaultdict
from decimal import Decimal

election_file = os.path.join('.', 'Resources', 'election_data.csv')

print(os.getcwd())
ID = []
County = []
Vote = []

with open(election_file, newline="") as electionCSV:

    electionReader = csv.reader(electionCSV, delimiter=",")

    # Skip the header line
    header = next(electionReader)

    for row in electionReader:
        ID.append(row[0])
        County.append(row[1])
        Vote.append(row[2])

totalVotes = len(ID) - 1
print('Election Results')
print('------------------------------------')
print(f'Total votes cast: {totalVotes}')

# Sort the Vote list alphabetically
# Then loop through, identifying if "i+1 == i".  If it is, add to the vote count for that person.
# Call the nominee by referring to the index[1]
# sortedVote = sorted(Vote)

# Find the unique values within the list by setting and converting back to list

uniqueVote = list(set(Vote))
print('------------------------------------')
print(f'Candidates receiving votes are: {uniqueVote}')
print('------------------------------------')

# Find out how many votes each candidate received
KhanCount = Vote.count("Khan")
CorreyCount = Vote.count("Correy")
ToolCount = Vote.count("O'Tooley")
LiCount = Vote.count("Li")

# Find percentages of each candidate, first need to convert our values into Decimals so the library can be accessed and used
KhanPerc = Decimal((KhanCount/totalVotes) * 100)
CorreyPerc = Decimal((CorreyCount/totalVotes) * 100)
ToolPerc = Decimal((ToolCount/totalVotes) * 100)
LiPerc = Decimal((LiCount/totalVotes) * 100)
# Then, we round the values up to only include up to 2 decimal places.
rKhanPerc = round(KhanPerc, 2)
rCorreyPerc = round(CorreyPerc, 2)
rToolPerc = round(ToolPerc, 2)
rLiPerc = round(LiPerc, 2)

# Find how many votes there were for each Candidate
print(f'Khan: {rKhanPerc}% {KhanCount}')
print(f'Correy: {rCorreyPerc}% {CorreyCount}')
print(f"O'Tooley: {rToolPerc}% ({ToolCount})")
print(f'Li: {rLiPerc}% ({LiCount})')
print('------------------------------------')

# Conditionals to compare which percentages were greater, whichever is the greatest is declared the winner.
if rKhanPerc > rCorreyPerc and rKhanPerc > rToolPerc and rKhanPerc > rLiPerc:
    print("Khan is the winner")
elif rCorreyPerc > rKhanPerc and rCorreyPerc  > rToolPerc and rCorreyPerc > rLiPerc:
    print("Correy is the winner")
elif rToolPerc > rKhanPerc and rToolPerc > rCorreyPerc and rToolPerc > rLiPerc:
    print("O'Tooley is the winner")
elif rLiPerc > rKhanPerc and rLiPerc > rCorreyPerc and rLiPerc > rToolPerc:
    print("Li is the winner")
else:
    print("Nobody won; Russia is new leader")

#outputFile = open('./Output.text', 'w', newline='')
#outputFile.write('Election Results')
#outputFile.write("\n")
#outputFile.write('------------------------------------')
#outputFile.write('\n')
#outputFile.write(f'Khan: {rKhanPerc}% {KhanCount}')
#outputFile.write('\n')
#outputFile.write(f'Correy: {rCorreyPerc}% {CorreyCount}')
#outputFile.write('\n')
#outputFile.write(f"O'Tooley: {rToolPerc}% {ToolCount}")
#outputFile.write('\n')
#outputFile.write(f'Li: {rLiPerc}% {LiCount}')
#outputFile.write('\n')
#outputFile.write('------------------------------------')
#outputFile.write('\n')
#if rKhanPerc > rCorreyPerc and rKhanPerc > rToolPerc and rKhanPerc > rLiPerc:
#    outputFile.write("Khan is the winner")
#elif rCorreyPerc > rKhanPerc and rCorreyPerc  > rToolPerc and rCorreyPerc > rLiPerc:
#    outputFile.write("Correy is the winner")
#elif rToolPerc > rKhanPerc and rToolPerc > rCorreyPerc and rToolPerc > rLiPerc:
#    outputFile.write("O'Tooley is the winner")
#elif rLiPerc > rKhanPerc and rLiPerc > rCorreyPerc and rLiPerc > rToolPerc:
#    outputFile.write("Li is the winner")
#else:
#    outputFile.write("Nobody won; Russia is new leader")
#outputFile.close()

outputFile = open('./Output.text', 'w', newline='')
outputFile.write('Election Results')

outputFile.write('------------------------------------\n')

outputFile.write(f'Khan: {rKhanPerc}% {KhanCount}\n')

outputFile.write(f'Correy: {rCorreyPerc}% {CorreyCount}\n')

outputFile.write(f"O'Tooley: {rToolPerc}% {ToolCount}\n")

outputFile.write(f'Li: {rLiPerc}% {LiCount}\n')

outputFile.write('------------------------------------\n')

if rKhanPerc > rCorreyPerc and rKhanPerc > rToolPerc and rKhanPerc > rLiPerc:
    outputFile.write("Khan is the winner")
elif rCorreyPerc > rKhanPerc and rCorreyPerc  > rToolPerc and rCorreyPerc > rLiPerc:
    outputFile.write("Correy is the winner")
elif rToolPerc > rKhanPerc and rToolPerc > rCorreyPerc and rToolPerc > rLiPerc:
    outputFile.write("O'Tooley is the winner")
elif rLiPerc > rKhanPerc and rLiPerc > rCorreyPerc and rLiPerc > rToolPerc:
    outputFile.write("Li is the winner")
else:
    outputFile.write("Nobody won; Russia is new leader")
outputFile.close()