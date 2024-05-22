#!/usr/bin/python
"""Advent of Code 2018, Day 18, Part 1

https://adventofcode.com/2018/day/18

Given a lumber map of empty spaces, trees, and lumberyards, simulate how
the acreage changes in make-up. Calculate score after 10 cycles.

See test.dat for sample data and lumber.dat for full data.

Author: Tim Behrendsen
"""

from collections import defaultdict

fn = 'test.dat'
fn = 'lumber.dat'

def main():
    with open(fn, 'r') as file:
        lumber = [ line.rstrip("\n") for line in file ]
    num_rows = len(lumber)
    num_cols = len(lumber[0])

    def get(l, r, c):
        return l[r][c] if 0 <= r < num_rows and 0 <= c < num_cols else '.'

    for i in range(10):
        new_lumber = []
        for r in range(num_rows):
            new_row = []
            for c in range(num_rows):
                counts = defaultdict(int)
                for dr, dc in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
                    counts[get(lumber, r+dr, c+dc)] += 1

                acre = lumber[r][c]
                if acre == '.':
                    if counts['|'] >= 3:
                        acre = '|'
                elif acre == '|':
                    if counts['#'] >= 3:
                        acre = '#'
                else:               # Must be lumberyard
                    if not (counts['#'] >= 1 and counts['|'] >= 1):
                        acre = '.'

                new_row.append(acre)
            new_lumber.append(''.join(new_row))
        lumber = new_lumber

    counts = defaultdict(int)
    for r in range(num_rows):
        for c in range(num_rows):
            counts[lumber[r][c]] += 1

    return counts['#'] * counts['|']

answer = main()
print(f"Answer is {answer}")
