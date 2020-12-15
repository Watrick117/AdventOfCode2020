#!/usr/bin/python3
"""Patrick Woltman

--- Part Two ---

The final step in breaking the XMAS encryption relies on the invalid number you just found: you must find a contiguous set of at least two numbers in your list which sum to the invalid number from step 1.

Again consider the above example:

35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576

In this list, adding up all of the numbers from 15 through 40 produces the invalid number from step 1, 127. (Of course, the contiguous set of numbers in your actual list might be much longer.)

To find the encryption weakness, add together the smallest and largest number in this contiguous range; in this example, these are 15 and 47, producing 62.

What is the encryption weakness in your XMAS-encrypted list of numbers?
"""

def encryption_weakness(cypher, invalid_index):

    for i in range(0, invalid_index):
        for j in range(0, invalid_index):
            if sum(cypher[i:j]) == int(cypher[invalid_index]):
                temp = cypher[i:j]
                temp.sort()

    return (temp[0], temp[-1])

def cyper_cracker(cypher, preamble_input):

    for i in range(0, len(cypher)-preamble_input):

        if int(cypher[i+preamble_input]) not in list(preamble_walkthru(cypher, i, i + preamble_input)):
            weakness = cypher[i+preamble_input]

    return weakness

def preamble_walkthru(cypher, start, end):

    temp = []
    preamble = []

    for i in range(start, end):
        temp.append(int(cypher[i]))

    for i in range(0, len(temp)):
        for j in range(0, len(temp)):
            if temp[i] != temp[j] and int(temp[i]) + int(temp[j]) not in preamble:
                preamble.append(int(temp[i]) + int(temp[j]))

    return preamble

import sys

# Takes in 'preamble_sample.txt' as cypher_sample
file1 = open('preamble_sample.txt', 'r') 
cypher_sample = file1.read().splitlines()
file1.close()

for i in range(0, len(cypher_sample)):
    cypher_sample[i] = int(cypher_sample[i])

# Takes in 'preamble.txt' as cypher
file1 = open('preamble.txt', 'r') 
cypher_puzzle = file1.read().splitlines()
file1.close()

for i in range(0, len(cypher_puzzle)):
    cypher_puzzle[i] = int(cypher_puzzle[i])

print()
print('cyper_sample')
print('The first number in the encryption that is out of order is: %s' % cyper_cracker(cypher_sample, 5))
print('The index of the invalid number is: %s' % cypher_sample.index(cyper_cracker(cypher_sample, 5)))
print('The smallest and largest number in this contiguous range is: %s and %s' % encryption_weakness(cypher_sample, cypher_sample.index(cyper_cracker(cypher_sample, 5))))
print('The sum of the smallest and largest number is: %s' % sum(encryption_weakness(cypher_sample, cypher_sample.index(cyper_cracker(cypher_sample, 5)))))


print()
print('cypher_puzzle')
print('The first number in the encryption that is out of order is: %s' % cyper_cracker(cypher_puzzle, 25))
print('The index of the invalid number is: %s' % cypher_puzzle.index(cyper_cracker(cypher_puzzle, 25)))
print('The smallest and largest number in this contiguous range is: %s and %s' % encryption_weakness(cypher_puzzle, cypher_puzzle.index(cyper_cracker(cypher_puzzle, 25))))
print('The sum of the smallest and largest number is: %s' % sum(encryption_weakness(cypher_puzzle, cypher_puzzle.index(cyper_cracker(cypher_puzzle, 25)))))

sys.exit()
