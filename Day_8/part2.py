#!/usr/bin/python3
"""Patrick Woltman
--- Part Two ---

After some careful analysis, you believe that exactly one instruction is corrupted.

Somewhere in the program, either a jmp is supposed to be a nop, or a nop is supposed to be a jmp. (No acc instructions were harmed in the corruption of this boot code.)

The program is supposed to terminate by attempting to execute an instruction immediately after the last instruction in the file. By changing exactly one jmp or nop, you can repair the boot code and make it terminate correctly.

For example, consider the same program from above:

nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6

If you change the first instruction from nop +0 to jmp +0, it would create a single-instruction infinite loop, never leaving that instruction. If you change almost any of the jmp instructions, the program will still eventually find another jmp instruction and loop forever.

However, if you change the second-to-last instruction (from jmp -4 to nop -4), the program terminates! The instructions are visited in this order:

nop +0  | 1
acc +1  | 2
jmp +4  | 3
acc +3  |
jmp -3  |
acc -99 |
acc +1  | 4
nop -4  | 5
acc +6  | 6

After the last instruction (acc +6), the program terminates by attempting to run the instruction below the last instruction in the file. With this change, after the program terminates, the accumulator contains the value 8 (acc +1, acc +1, acc +6).

Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp). What is the value of the accumulator after the program terminates?
"""
import sys

# file input
#df = pd.read_fwf('boot_code_sample.txt', sep=" ", header=None, names=['Operation','Argument', 'Accumulator'])

file1 = open('boot_code.txt', 'r') 
unsorted = file1.read().splitlines()
file1.close()

boot_code = []

# Splits unsorted and adds it to boot_code
for i in range(0, len(unsorted)):
    temp = [unsorted[i].split()[0], unsorted[i].split()[1] , 0]
    boot_code.append((temp))
    #boot_code.append(0)

line = 0
accumulator = 0
history = []

for i in range(0, len(boot_code)):
    print('%s --------- %s' % (boot_code[i][1][:1], boot_code[i][1][1:]))

while True:
    print(f'{boot_code[line] = }')

    if line in history:
        print()
        print()
        print()
        print()
        print('***************')
        print(f'{boot_code[line] = }')
        print('***************')
        print()
        print()
        print(f'{history = }')
        print()

        break

    history.append(line)

    if boot_code[line][0] == 'nop':
        print('     nop')
        line += 1
    elif boot_code[line][0] == 'acc':
        print('     acc')
        if boot_code[line][1][:1] == '+':
            print('+')
            boot_code[line][2] += int(boot_code[line][1][1:])
            accumulator += int(boot_code[line][1][1:])
            line += 1
        elif boot_code[line][1][:1] == '-':
            print('-')
            boot_code[line][2] -= int(boot_code[line][1][1:])
            accumulator -= int(boot_code[line][1][1:])
            line += 1
        #boot_code[line][0][2]
    elif boot_code[line][0] == 'jmp':
        print('     jmp')
        if boot_code[line][1][:1] == '+':
            print('+')
            line += int(boot_code[line][1][1:])
        elif boot_code[line][1][:1] == '-':
            print('-')
            line -= int(boot_code[line][1][1:])

    print(f'{boot_code[line-1] = }')
    print('-----------------------------------')

# Prints the whole boot_code list by line
for i in range(0, len(boot_code)):
    print(f'{boot_code[i] = }')

#print(f'{boot_code = }')

print(f'{accumulator = }')
print()

sys.exit()
