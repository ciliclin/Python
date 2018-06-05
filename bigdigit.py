#!/usr/bin/python3

import sys

zero = [" ** ",
        "*  *",
        "*  *",
        " ** "]
one = ["  **  ",
       "   *  ",
       "   *  ",
       "  *** "]
print(zero, one)

DIGIT = [ zero, one ]

try:
    digits = sys.argv[1]
    print(digits)

    row = 0
    while row < 4:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = DIGIT[number]
            line += digit[row]+" "
            column += 1
        print(line)
        row += 1
except IndexError:
    print("Usage:", sys.argv[0], " <number>")
except ValueError as err:
    print(err, "in", digits)
    
