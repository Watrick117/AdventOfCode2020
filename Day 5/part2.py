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

highest_seadID = -1
lowest_seadID = 1000

for i in range(0, len(passes)):
    row = recursive_delete(passes[i][:7],0, 0, 127)
    column = recursive_delete(passes[i][7:], 0, 0, 7)
    seatID = row * 8 + column

    if highest_seadID < seatID:
        highest_seadID = seatID
    
    if lowest_seadID > seatID:
        lowest_seadID = seatID

    temp = [row, column, seatID]

    seating_info.append(temp)

print()

seating_info.sort()

#Prints seating info
for i in range(0, len(seating_info)):
    print(seating_info[i])

#Finds missing seats

expected_seatID = lowest_seadID

for i in range(0, len(seating_info)):
    debug_seating_info = seating_info[i][2]
    debug_expected_seatID = expected_seatID
    if seating_info[i][2] != expected_seatID:
        print()
        print()
        print('The missing sead ID is == %s' % (int(seating_info[i][2])-1))
        i += 1
        expected_seatID += 1
    expected_seatID += 1
    if expected_seatID == 8:
        expected_seatID = 0

sys.exit()
