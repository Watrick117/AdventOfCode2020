#!/usr/bin/python3
"""Patrick Woltman
Day 2 of Advent of Code 2020

--- Part Two ---

While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

    1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

How many passwords are valid according to the new interpretation of the policies?

"""

import csv
import numpy as np
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
    
    # Numpy is the only way I know how to use logical xor
    if np.logical_xor(passwords[j][2][int(temp[0])-1:int(temp[0])] == str(passwords[j][1]) , passwords[j][2][int(temp[1])-1:int(temp[1])] == str(passwords[j][1])):
        validPasswords += 1
    else:
        invalidPasswords += 1

print()
print(f'{invalidPasswords = }')
print(f'{validPasswords = }')

sys.exit()
