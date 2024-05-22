#!/usr/bin/python
"""Advent of Code 2018, Day 1, Part 2

https://adventofcode.com/2018/day/1

Given a list of "changes in frequency", calculate the sum total, and find
the first frequence that repeats after cycling the list in a loop

See changes.dat for full data.

Author: Tim Behrendsen
"""

fn = 'changes.dat'

import re

def main():
    # Read in number list
    with open(fn, 'r') as file:
        num_list = [ int(line.rstrip("\n")) for line in file ]

    repeats = set()
    total = 0
    while True:
        for n in num_list:
            total += n
            if total in repeats:
                return total
            repeats.add(total)

answer = main()
print(f"Answer is {answer}")
