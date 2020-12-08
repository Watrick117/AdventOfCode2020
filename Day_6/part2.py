#!/usr/bin/python3
"""Patrick Woltman
--- Part Two ---

As you finish the last group's customs declaration, you notice that you misread one word in the instructions:

You don't need to identify the questions to which anyone answered "yes"; you need to identify the questions to which everyone answered "yes"!

Using the same example as above:

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

    In the first group, everyone (all 1 person) answered "yes" to 3 questions: a, b, and c.
    In the second group, there is no question to which everyone answered "yes".
    In the third group, everyone answered yes to only 1 question, a. Since some people did not answer "yes" to b or c, they don't count.
    In the fourth group, everyone answered yes to only 1 question, a.
    In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.

In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

For each group, count the number of questions to which everyone answered "yes". What is the sum of those counts?
"""

"""
Materials Used:
    https://pymotw.com/2/collections/counter.html
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
    if unsorted[i] != '':
        temp.append(unsorted[i])
    elif unsorted[i] == '':
        declarations.append(temp.copy()) # adds temp to declaration NOT by refferance but an actual copy of the list
        temp.clear()

testtest = ''

# Walks thru every person and every group and counts the number of yes's they have answered
for group in range(0, len(declarations)):
    for person in range(0, len(declarations[group])):
        #for answer in range(0, len(declaration[group][person])): 
        debug_temp = declarations[group][person]
        temp += declarations[group][person]
        testtest += declarations[group][person]
    
    # Counts the elements in a list after all duplicates have been deleted
    debug_sums_per_group = len(list(dict.fromkeys(temp)))

    # Removes duplicates from temp and counts the how many there are
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

sys.exit()
