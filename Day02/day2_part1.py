#!/usr/bin/python
"""Advent of Code 2018, Day 2, Part 1

https://adventofcode.com/2018/day/2

For list of box IDs, figure out which ones have exactly two of the same
letter and three of the same letter.

See boxes.dat for full data.

Author: Tim Behrendsen
"""

fn = 'boxes.dat'

from collections import defaultdict

def main():
    # Read in number list
    with open(fn, 'r') as file:
        box_list = [ line.rstrip("\n") for line in file ]

    total_2 = 0
    total_3 = 0
    for box in box_list:
        counts = defaultdict(int)
        for c in box:
            counts[c] += 1
        num_2 = len([ n for n in counts.values() if n == 2 ])
        total_2 += num_2 != 0
        num_3 = len([ n for n in counts.values() if n == 3 ])
        total_3 += num_3 != 0

    return total_2 * total_3


answer = main()
print(f"Answer is {answer}")
