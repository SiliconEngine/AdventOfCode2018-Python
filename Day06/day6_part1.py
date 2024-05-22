#!/usr/bin/python
"""Advent of Code 2018, Day 6, Part 1

https://adventofcode.com/2018/day/6

Given a list of coordinates, figure out the size of the largest area that
is furthest away from all points (manhattan distance), while being within
the coordinates.

See test.dat for sample data and coord.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'coord.dat'

import re

def main():
    c_list = []
    with open(fn, 'r') as file:
        for line in file:
            m = re.findall(r'\d+', line)
            c_list.append((int(m[0]), int(m[1])))

    # Calculate min/max of coordinates
    min_x, max_x = min([ x for x, y in c_list]), max([ x for x, y in c_list])
    min_y, max_y = min([ y for x, y in c_list]), max([ y for x, y in c_list])

    # Within the min/max, figure out which coordinate is closest
    totals = [0] * len(c_list)
    for y in range(min_x, max_x+1):
        for x in range(min_x, max_x+1):
            min_dist = 99999
            min_idx = -1
            min_count = 0
            for idx, c in enumerate(c_list):
                dist = abs(c[0] - x) + abs(c[1] - y)
                if dist == min_dist:
                    min_count += 1
                elif dist < min_dist:
                    min_idx = idx
                    min_count = 1
                    min_dist = dist

            # Only add to coordinate total if no other coordinate same distance
            if min_count == 1:
                totals[min_idx] += 1

    # Find best total for coordinate that is within the grid (not at one of the edges)
    best_total, best_idx = 0, -1
    for idx, c in enumerate(c_list):
        if c[0] not in (min_x, max_x) and c[1] not in (min_y, max_y):
            if totals[idx] > best_total:
                best_total, best_idx = totals[idx], idx

    return best_total

answer = main()
print(f"Answer is {answer}")
