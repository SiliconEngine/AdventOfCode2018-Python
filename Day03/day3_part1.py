#!/usr/bin/python
"""Advent of Code 2018, Day 3, Part 1

https://adventofcode.com/2018/day/3

Given a list of "claims", which are coordinates of a rectangle within a
1000x1000 sheet of cloth, figure out how many squares overlap.

See test.dat for sample data and claims.dat for full data.

Author: Tim Behrendsen
"""

fn = 'claims.dat'

import re

def main():
    # Read in claims

    claims = []
    with open(fn, 'r') as file:
        for line in file:
            matches = re.findall(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line)[0]
            claims.append([ int(n) for n in matches[1:5] ])

    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    for claim in claims:
        for x in range(claim[0], claim[0] + claim[2]):
            for y in range(claim[1], claim[1] + claim[3]):
                grid[y][x] += 1

    total = 0
    for y in range(1000):
        total += len([ n for n in grid[y] if n > 1 ])

    return total

answer = main()
print(f"Answer is {answer}")
