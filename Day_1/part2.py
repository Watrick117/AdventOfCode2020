#!/usr/bin/python3
"""Patrick Woltman
Day 1 part 2 of Advent of Code 2020
"""

import csv
import sys

with open("expense_report.csv","r") as csvFile:
  reader = csv.reader(csvFile)
  data = []
  for row in reader:
     if len(row) !=0:
        data = data + row
csvFile.close()

print(f'{len(data) = }')
print()
print(data)
print()

for i in range(1, len(data)+1):
    for j in range(1, len(data)+1):
        for k in range(1, len(data)+1):

            duplicates = [int(data[i-1]), int(data[j-1]), int(data[k-1])]

            if len(set(duplicates)) != len(duplicates):
                break
                
            if int(data[i-1]) + int(data[j-1]) + int(data[k-1]) == 2020:
                print('There are three expenses that add up to 2020. They are %s, %s and %s.' % (data[i-1],data[j-1],data[k-1]))
                print('And the product of their multiplication is %s' % (int(data[i-1]) * int(data[j-1]) * int(data[k-1])))
                print()

sys.exit()
