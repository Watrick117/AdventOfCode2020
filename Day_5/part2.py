#!/usr/bin/python3
"""Patrick Woltman
--- Part Two ---

Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.

Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

What is the ID of your seat?
"""

import sys

def recursive_delete(boarding_pass, index, low, high):

    string = boarding_pass
    boarding_pass_index = boarding_pass[index]
    size_of_boarding_pass = (high-low+1)
    size_of_boarding_pass_by_2 = (high-low+1) / 2

    if high - low == 1:
        if boarding_pass[index] == 'F' or boarding_pass[index] == 'L':
            return low
        elif boarding_pass[index] == 'B' or boarding_pass[index] == 'R':
            return high

    if boarding_pass[index] == 'F' or boarding_pass[index] == 'L':
        return recursive_delete(boarding_pass, index + 1, low, high-( int((high-low+1) / 2)))
    elif boarding_pass[index] == 'B' or boarding_pass[index] == 'R':
        return recursive_delete(boarding_pass, index + 1, low+( int((high-low+1) / 2)), high)

seating_info = []
# Takes in separate lines from .txt (read only) and saves them to passes
fileObj = open('boarding_passes.txt', "r")
passes = fileObj.read().splitlines()
fileObj.close()

# Prints full Boarding Passes
for i in range(0, len(passes)):
    print(passes[i])


# Walk thru the list of boarding passes calculate the row, column, and seat ID

highest_seatID = 0

for i in range(0, len(passes)):
    row = recursive_delete(passes[i][:7],0, 0, 127)
    column = recursive_delete(passes[i][7:], 0, 0, 7)
    seatID = row * 8 + column

    if highest_seatID < seatID:
        highest_seatID = seatID

    temp = [passes[i], row, column, seatID]

    seating_info.append(temp)

print()

for i in range(0, len(seating_info)):
    print(seating_info[i])

print()
print('The highest sead ID on a boarding pass == %s' % highest_seatID)

sys.exit()
