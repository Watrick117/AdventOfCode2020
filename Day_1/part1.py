#!/usr/bin/python3
"""Patrick Woltman
Day 1 part 1 of Advent of Code 2020
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

        if int(data[i-1]) == int(data[j-1]):
            break
            
        if int(data[i-1]) + int(data[j-1]) == 2020:
            data_i_plus_data_j = int(data[i-1]) * int(data[j-1])
            print('The two expenses that add up to 2020. Are %s and %s.' % (data[i-1],data[j-1]))
            print('And the product of their multiplication is %s' % (int(data[i-1]) * int(data[j-1])))
            print()

sys.exit()
