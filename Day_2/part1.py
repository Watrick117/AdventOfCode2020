#!/usr/bin/python3
"""Patrick Woltman
Day 2 part 1 of Advent of Code 2020
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

print(f'{len(passwords) = }')
print()

for i in range(0, len(passwords)):
    passwords[i] = passwords[i].split(" ")
    passwords[i][1] = passwords[i][1].replace(':', '')

    
for j in range(0, len(passwords)):
    print()
    print(f'{j = }')

    temp = passwords[j][0].split("-")

    count = 0

    for x in range(0, len(passwords[i][2])):

        if passwords[j][2][x:x+1] == str(passwords[j][1]):
            count += 1

    if  int(temp[0]) <= count <= int(temp[1]):
        validPasswords += 1
        print("VALID")
    elif count < int(temp[0]) or count > int(temp[1]):
        invalidPasswords += 1
        print("INVALID")

    print(f'{passwords[j][2] = }')

    print(count >= int(temp[0]) <= int(temp[1]))
    print(f'{temp = }')
    print(f'{passwords[j][1] = }')
    print(f'{count = }')

    if (count >= int(temp[0]) <= int(temp[1])) == True and (count < int(temp[0]) < int(temp[1])) == True:
        input('Whats wrong with this section.\n')

print()
print(f'{invalidPasswords = }')
print(f'{validPasswords = }')

programWorked = len(passwords) - invalidPasswords - validPasswords
if programWorked == 0:
    print("Program Worked")

sys.exit()
