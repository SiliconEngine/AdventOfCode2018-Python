#!/usr/bin/python
"""Advent of Code 2018, Day 3, Part 2

https://adventofcode.com/2018/day/3

Given a list of "claims", which are coordinates of a rectangle within a
1000x1000 sheet of cloth, figure out which one doesn't overlap any of them.

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
            claims.append([ int(n) for n in matches ])

    # Test if two ranges intersect
    def intersect(a1, a2, b1, b2): return max(a1, b1) < min(a2, b2)

    # Mark all the claims that intersect with a different one
    bad_set = set()
    for idx1 in range(len(claims)):
        for idx2 in range(idx1+1, len(claims)):
            c1, c2 = claims[idx1], claims[idx2]
            if intersect(c1[1], c1[1]+c1[3], c2[1], c2[1]+c2[3]) \
                    and intersect(c1[2], c1[2]+c1[4], c2[2], c2[2]+c2[4]):
                bad_set.add(idx1)
                bad_set.add(idx2)

    # Figure out which one never intersected another
    for idx in range(len(claims)):
        if idx not in bad_set:
            return claims[idx][0]

    return None

answer = main()
print(f"Answer is {answer}")
