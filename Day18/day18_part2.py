#!/usr/bin/python
"""Advent of Code 2018, Day 18, Part 2

https://adventofcode.com/2018/day/18

Given a lumber map of empty spaces, trees, and lumberyards, simulate how
the acreage changes in make-up. For Part 2, simulate 1000000000 cycles

See test.dat for sample data and lumber.dat for full data.

Author: Tim Behrendsen
"""

from collections import defaultdict
import itertools

fn = 'test.dat'
fn = 'lumber.dat'

target = 1000000000

def main():
    lumber = []
    with open(fn, 'r') as file:
        for line in file:
            lumber.append([ c for c in line.rstrip("\n") ])
    num_rows, num_cols = len(lumber), len(lumber[0])

    def get(l, r, c):
        return l[r][c] if 0 <= r < num_rows and 0 <= c < num_cols else '.'

    # Contine simulating the changes, until we see a pattern repeat
    values, seen = [ 0 ], { }
    for i in itertools.count(1):
        if (h := hash(''.join(c for row in lumber for c in row))) in seen:
            break
        seen[h] = i

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
            new_lumber.append(new_row)

        lumber = new_lumber
        counts = defaultdict(int)
        for r in range(num_rows):
            for c in range(num_rows):
                counts[lumber[r][c]] += 1
        values.append(counts['#'] * counts['|'])

    cycle_len = i - seen[h]
    cycle_base = (i // cycle_len - 1) * cycle_len
    return values[cycle_base + target % cycle_len]

answer = main()
print(f"Answer is {answer}")
