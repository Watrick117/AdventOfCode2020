#!/usr/bin/python3
"""Patrick Woltman

--- Day 3: Toboggan Trajectory ---

--- Part Two ---

Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.

In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?
"""

import sys

fileObj = open('map.txt', "r")
treemap = fileObj.read().splitlines()
fileObj.close()

for i in range(0, len(treemap)):
    print(treemap[i])

slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
#slopes = [(1,1),(1,3),(1,5),(1,7),(1,1)]

keepCount = []


print(slopes)
print(f'{len(treemap) = }')

for i in range(0,5):
    for j in range(0,2):
        print(slopes[i][j])

multitudeOfTrees = 1

for i in range(0, 5):

    print("For loop")
    x = 0
    y = 0

    count = 0

    #while x + 1 < len(treemap):
    for x in range(0, len(treemap)):

        #print(f'{treemap[i][x] = }')
        #print("While loop")

        x += slopes[i][1]
        y += slopes[i][0]
        
        #print()
        #print(f'{len(treemap) = }')
        #print(f'{treemap[x] = }')
        print(f'{slopes[i][0] = }')
        print(f'{slopes[i][1] = }')
        #print(f'{x = }')
        #print(f'{y = }')
        #print(f'{y % len(treemap[x]) = }')

        #print(len(treemap))
        #print(f'{x = }')

        """if x >= len(treemap):
            print()
            print('about to go over')
            print('x > len(treemap)')
            print(x)
            print()
        """

        if x > len(treemap) -1:
            break

        print(f'{treemap[x-1] = }')
        if treemap[x][ y % len(treemap[x]) ] == '#':
            count += 1

    print()
    print(f'{count = }')

    keepCount.append(count)
    multitudeOfTrees *= count
    print(f'{multitudeOfTrees = }')

print(f'{multitudeOfTrees = }')
print(f'{keepCount = }')

sys.exit()
