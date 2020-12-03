#!/usr/bin/python3
"""Patrick Woltman
--- Day 2: Password Philosophy ---

--- Part One ---

Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc

Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?

"""

import csv
import sys

with open("passwords.csv","r") as csvFile:
  reader = csv.reader(csvFile)
  passwords = []
  for row in reader:
     if len(row) !=0:
        passwords = passwords + row 
csvFile.close()

validPasswords = 0
invalidPasswords = 0

for i in range(0, len(passwords)):
    passwords[i] = passwords[i].split(" ")
    passwords[i][1] = passwords[i][1].replace(':', '')

    
for j in range(0, len(passwords)):

    temp = passwords[j][0].split("-")

    count = 0

    for x in range(0, len(passwords[i][2])):

        if passwords[j][2][x:x+1] == str(passwords[j][1]):
            count += 1

    if  int(temp[0]) <= count <= int(temp[1]):
        validPasswords += 1
    elif count < int(temp[0]) or count > int(temp[1]):
        invalidPasswords += 1

print()
print(f'{invalidPasswords = }')
print(f'{validPasswords = }')

sys.exit()
