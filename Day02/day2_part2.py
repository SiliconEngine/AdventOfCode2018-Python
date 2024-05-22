#!/usr/bin/python
"""Advent of Code 2018, Day 2, Part 2

https://adventofcode.com/2018/day/2

For list of boxes, figure out what pair have exactly one letter difference, then
output common letters between those two.

See test.dat for sample data and boxes.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'boxes.dat'

from collections import defaultdict

def main():
    # Read in number list
    with open(fn, 'r') as file:
        box_list = [ line.rstrip("\n") for line in file ]

    # Find pair of boxes that differ by one letter
    for idx1 in range(len(box_list)):
        for idx2 in range(idx1+1, len(box_list)):
            box1, box2 = box_list[idx1], box_list[idx2]
            diffs = [ chkidx for chkidx, c in enumerate(box1) if c != box2[chkidx] ]
            if len(diffs) == 1:
                # Figure out what letters in common
                return ''.join([ c for chkidx, c in enumerate(box1) if c == box2[chkidx] ])

answer = main()
print(f"Answer is {answer}")
