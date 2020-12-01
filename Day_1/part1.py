#!/usr/bin/python3
"""Patrick Woltman
Day 1 part 1 of Advent of Code 2020
"""

import csv
with open('expense_report.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row)