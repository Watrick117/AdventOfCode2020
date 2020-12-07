#!/usr/bin/python3
"""Patrick Woltman

--- Part Two ---

The line is moving more quickly now, but you overhear airport security talking about how passports with invalid data are getting through. Better add some data validation, quick!

You can continue to ignore the cid field, but each other field has strict rules about what values are valid for automatic validation:

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.

Your job is to count the passports where all required fields are both present and valid according to the above rules. Here are some example values:

byr valid:   2002
byr invalid: 2003

hgt valid:   60in
hgt valid:   190cm
hgt invalid: 190in
hgt invalid: 190

hcl valid:   #123abc
hcl invalid: #123abz
hcl invalid: 123abc

ecl valid:   brn
ecl invalid: wat

pid valid:   000000001
pid invalid: 0123456789

Here are some invalid passports:

eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

Here are some valid passports:

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719

Count the number of valid passports - those that have all required fields and valid values. Continue to treat cid as optional. In your batch file, how many passports are valid?
"""

import sys

file1 = open('passports_invalid.bat', 'r') 
unsorted = file1.readlines() 

passports = []
dictionary_passports = {}
count = 0
is_valid = True
valid_count = 0

required_fields = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
    #'cid' #has been removed to let North Pole Credentials get thru the passport checks
]

eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
hcl_safe_chars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

valid_passports = 0
temp = ''

for i in range(0, len(unsorted)):
    if unsorted[i] != '\n':
        #temp = str(temp + ' ' + unsorted[i]).replace(':', ' ').strip('\n')
        temp = str(temp + ' ' + unsorted[i]).strip('\n')
    elif unsorted[i] == '\n':
        passports.append(temp.strip().split())
        #print(f'{passports = }')
        temp = ''

print('---------------------------------------------------')

for i in range(0, len(passports)):
    for j in range(0, len(passports[i])):
        tempB = passports[i][j].replace(':', ' ').split(' ')
        dictionary_passports[tempB[0]] = tempB[1]
    print(f'{dictionary_passports = }')

    if 'byr' in dictionary_passports:
        print(dictionary_passports['byr'])
        if 1919 < int(dictionary_passports['byr']) < 2003:
            print('byr is good passport[%s]' % i)
    else:
        print('bry is wrong passport[%s]' % i)
        is_valid = False

    if 'iyr' in dictionary_passports:
        print(dictionary_passports['iyr'])
        if 2009 < int(dictionary_passports['iyr']) < 2021:
            print('iyr is good passport[%s]' % i)
    else:
        print('iyr is wrong passport[%s]' % i)
        is_valid = False

    if 'eyr' in dictionary_passports:
        print(dictionary_passports['eyr'])
        if 2019 < int(dictionary_passports['eyr']) < 2031:
            print('eyr is good passport[%s]' % i)
    else:
        print('eyr is wrong passport[%s]' % i)
        is_valid = False

    if 'hgt' in dictionary_passports:
        print(dictionary_passports['hgt'])
        if dictionary_passports['hgt'].endswith('cm'):
            if 150 < int(dictionary_passports['hgt'].strip('cm')) < 193:
                print('hgt is good passport[%s]' % i)
        elif dictionary_passports['hgt'].endswith('in'):
            if 59 < int(dictionary_passports['hgt'].strip('in')) < 76:
                print('hgt is good passport[%s]' % i)
    else:
        print('hgt is wrong passport[%s]' % i)
        is_valid = False

    if 'hcl' in dictionary_passports:
        print(dictionary_passports['hcl'])
        if dictionary_passports['hcl'][0] == '#' and len(dictionary_passports['hcl'][1:]) == 6:
            for i in range(0, len(dictionary_passports['hcl'])):
                if dictionary_passports['hcl'][i] in hcl_safe_chars:
                    count += 1
            if count == 6:
                print('hcl is good passport[%s]' % i)
            else: is_valid = False
        else: is_valid = False
        count = 0
    else:
        print('hcl is wrong passport[%s]' % i)
        is_valid = False
    
    if 'ecl' in dictionary_passports:
        print(dictionary_passports['ecl'])
        if dictionary_passports['ecl'] in eye_colors:
            print('ecl is good passport[%s]' % i)
    else:
        print('ecl is wrong passport[%s]' % i)
        is_valid = False

    if 'pid' in dictionary_passports:
        print(dictionary_passports['pid'])
        if len(dictionary_passports['pid']) == 9:
            print('pid is good passport[%s]' % i)
    else:
        print('pid is wrong passport[%s]' % i)
        is_valid = False

    """
    try:
        if 1919 < int(dictionary_passports['byr']) < 2003:
            print(dictionary_passports['byr'])
            print('byr is good passport[%s]' % i)
    except:
        print('bry is wrong passport[%s]' % i)
        is_valid = False

    try:
        if 2009 < int(dictionary_passports['iyr']) < 2021:
            print(dictionary_passports['iyr'])
            print('iyr is good passport[%s]' % i)
    except:
        print('iyr is wrong passport[%s]' % i)
        is_valid = False

    try:
        if 2019 < int(dictionary_passports['eyr']) < 2031:
            print(dictionary_passports['eyr'])
            print('eyr is good passport[%s]' % i)
    except:
        print('eyr is wrong passport[%s]' % i)
        is_valid = False

    try:
        if dictionary_passports['hgt'].endswith('cm'):
            if 150 < int(dictionary_passports['hgt'].strip('cm')) < 193:
                print(dictionary_passports['hgt'])
                print('hgt is good passport[%s]' % i)
        elif dictionary_passports['hgt'].endswith('in'):
            if 59 < int(dictionary_passports['hgt'].strip('in')) < 76:
                print(dictionary_passports['hgt'])
                print('hgt is good passport[%s]' % i)
    except:
        print('hgt is wrong passport[%s]' % i)
        is_valid = False

    try:
        print(dictionary_passports['hcl'][1:])
        print(dictionary_passports['hcl'][1:])
        print(dictionary_passports['hcl'][1:])
        print(dictionary_passports['hcl'][1:])
        print(dictionary_passports['hcl'][1:])
        print(dictionary_passports['hcl'][1:])
        print(dictionary_passports['hcl'][1:])
        print(dictionary_passports['hcl'][1:])
    except:
        print('88888888888888888888888888888')
        print('88888888888888888888888888888')
        print('88888888888888888888888888888')
        print('88888888888888888888888888888')
        print('88888888888888888888888888888')
        print('88888888888888888888888888888')
        print('88888888888888888888888888888')
        print('88888888888888888888888888888')
        print('88888888888888888888888888888')

    try:
        if dictionary_passports['hcl'][0] == '#' and len(dictionary_passports['hcl'][1:]) == 6:
            for i in range(0, len(dictionary_passports['hcl'])):
                if dictionary_passports['hcl'][i] in hcl_safe_chars:
                    count += 1
                if count == 6:
                    print(dictionary_passports['hcl'])
                    print('hcl is good passport[%s]' % i)
        count = 0
    except:
        print('hcl is wrong passport[%s]' % i)
        is_valid = False
    
    try:
        if dictionary_passports['ecl'] in eye_colors:
            print(dictionary_passports['ecl'])
            print('ecl is good passport[%s]' % i)
    except:
        print('ecl is wrong passport[%s]' % i)
        is_valid = False

    try:
        if len(dictionary_passports['pid']) == 9:
            print(dictionary_passports['pid'])
            print('pid is good passport[%s]' % i)
    except:
        print('pid is wrong passport[%s]' % i)
        is_valid = False
    """

    dictionary_passports.clear()

    print(f'{is_valid = }')

    if is_valid == True:
        valid_count += 1
        print('this passport is valid!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    elif is_valid == False:
        print('this passport ERRORED*********************************************************************************')
    
    print(f'{valid_count = }')
    is_valid = True
    print('---------------------------------------------------')
    
print(f'{valid_count = }')
print('---------------------------------------------------')
print(f'{len(passports) = }')
print('---------------------------------------------------')
#print(f'{passports[258] = }')

print()

sys.exit()

"""
tried:
    99
    102 it is too high
    107 it is too high
"""
