#!/usr/bin/python3
"""Patrick Woltman
--- Day 6: Custom Customs ---

As your flight approaches the regional airport where you'll switch to a much larger plane, customs declaration forms are distributed to the passengers.

The form asks a series of 26 yes-or-no questions marked a through z. All you need to do is identify the questions for which anyone in your group answers "yes". Since your group is just you, this doesn't take very long.

However, the person sitting next to you seems to be experiencing a language barrier and asks if you can help. For each of the people in their group, you write down the questions for which they answer "yes", one per line. For example:

abcx
abcy
abcz

In this group, there are 6 questions to which anyone answered "yes": a, b, c, x, y, and z. (Duplicate answers to the same question don't count extra; each question counts at most once.)

Another group asks for your help, then another, and eventually you've collected answers from every group on the plane (your puzzle input). Each group's answers are separated by a blank line, and within each group, each person's answers are on a single line. For example:

abc

a
b
c

ab
ac

a
a
a
a

b

This list represents answers from five groups:

    The first group contains one person who answered "yes" to 3 questions: a, b, and c.
    The second group contains three people; combined, they answered "yes" to 3 questions: a, b, and c.
    The third group contains two people; combined, they answered "yes" to 3 questions: a, b, and c.
    The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
    The last group contains one person who answered "yes" to only 1 question, b.

In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.

For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?
"""

import sys

# file input
file1 = open('declarations.txt', 'r') 
unsorted = file1.read().splitlines()
file1.close()

declarations = []
temp = []
sums = []

# Walks thru the unsorted information and files them in to a list of lists
for i in range(0, len(unsorted)):
    debug_unsorted = unsorted[i]
    #print(unsorted[i])
    if unsorted[i] != '':
        temp.append(unsorted[i])
    elif unsorted[i] == '':
        declarations.append(temp.copy()) # adds temp to declaration NOT by refferance but an actual copy of the list
        temp.clear()

testtest = ''
# 
for group in range(0, len(declarations)):
    for person in range(0, len(declarations[group])):
        #for answer in range(0, len(declaration[group][person])): 
        debug_temp = declarations[group][person]
        temp += declarations[group][person]
        testtest += declarations[group][person]
        print(f'{temp = }')
    
    # Counts the elements in a list after all duplicates have been deleted
    debug_sums_per_group = len(list(dict.fromkeys(temp)))
    
    print(f'{list(dict.fromkeys(temp)) = }')
    print(f'{len(list(dict.fromkeys(temp))) = }')
    print()
    sums.append(len(list(dict.fromkeys(temp))))
    temp = ''
    



# Displays the sorted infromation to the screen
print()
for group in range(0, len(declarations)):
    print(declarations[group])

print()
print(sums)

print()
print('The total number of all the groups of passangers is %s' % sum(sums))

print()
print(list(dict.fromkeys(testtest)))

print()
print(len(declarations))

print()
print(len(sums))

sys.exit()

"""
Tried:
6697 is too low
"""