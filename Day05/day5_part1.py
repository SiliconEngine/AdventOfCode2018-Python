#!/usr/bin/python
"""Advent of Code 2018, Day 5, Part 1

https://adventofcode.com/2018/day/5

Given a list of letters that make up a "polymer", eliminate sets of letters
that pair with opposite case (reacting and destroying themselves).

See test.dat for sample data and polymer.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'polymer.dat'

import re

def main():
    with open(fn, 'r') as file:
        polymer = [ c for c in file.readline().rstrip("\n") ]

    new_p = []
    for c in polymer:
        if len(new_p) and new_p[-1] != c and new_p[-1].upper() == c.upper():
            new_p.pop()
        else:
            new_p.append(c)

    return len(new_p)

answer = main()
print(f"Answer is {answer}")
