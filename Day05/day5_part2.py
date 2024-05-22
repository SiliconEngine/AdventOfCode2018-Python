#!/usr/bin/python
"""Advent of Code 2019, Day 5, Part 2

https://adventofcode.com/2019/day/5

Given a list of letters that make up a "polymer", eliminate sets of letters
that pair with opposite case (reacting and destroying themselves). For Part 2,
remove a letter and figure out which removal results in the smallest polymer
after reduction.

See test.dat for sample data and polymer.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'polymer.dat'

import re

def reduce(p):
    new_p = []
    for c in p:
        if len(new_p) and new_p[-1] != c and new_p[-1].upper() == c.upper():
            new_p.pop()
        else:
            new_p.append(c)
    return new_p

def main():
    with open(fn, 'r') as file:
        polymer = [ c for c in file.readline().rstrip("\n") ]

    # Figure out what letters are available
    letters = set([ c.lower() for c in polymer ])

    best_len = 999999
    for elim in letters:
        # Remove letter and reduce
        candidate = [ c for c in polymer if c.lower() != elim ]
        new_p = reduce(candidate)

        #print(f"Letter {elim} was {len(new_p)}")
        if len(new_p) < best_len:
            best_len = len(new_p)

    return best_len

answer = main()
print(f"Answer is {answer}")
