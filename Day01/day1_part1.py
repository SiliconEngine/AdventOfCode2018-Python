#!/usr/bin/python
"""Advent of Code 2018, Day 1, Part 1

https://adventofcode.com/2018/day/1

Given a list of "changes in frequency", calculate the sum total.

See changes.dat for full data.

Author: Tim Behrendsen
"""

fn = 'changes.dat'

import re

def main():
    # Read in number list
    with open(fn, 'r') as file:
        num_list = [ int(line.rstrip("\n")) for line in file ]
    return sum(num_list)

answer = main()
print(f"Answer is {answer}")
