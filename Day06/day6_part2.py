#!/usr/bin/python
"""Advent of Code 2018, Day 6, Part 2

https://adventofcode.com/2018/day/5

Given a list of coordinates, figure out the number of coordinates where the total of
the manhattan distance to all given coordinates is < 10000.

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

    min_x, max_x = min([ x for x, y in c_list]), max([ x for x, y in c_list])
    min_y, max_y = min([ y for x, y in c_list]), max([ y for x, y in c_list])

    start_x, start_y = (min_x + max_x)//2, (min_y + max_y)//2
    target_total = 32 if fn.startswith('test') else 10000

    # Check if total distance is less than target distance
    def check_coord(x, y):
        total = 0
        for c in c_list:
            total += abs(c[0] - x) + abs(c[1] - y)
        return total < target_total

    # Start in the center and move outward, checking coordinates
    last_coord_count = -1
    coord_count = check_coord(start_x, start_y)
    offset = 1
    while True:
        y1 = start_y - offset
        y2 = start_y + offset
        # Do top of rectangle and bottom
        for x in range(start_x - offset, start_x + offset + 1):
            coord_count += check_coord(x, y1)
            coord_count += check_coord(x, y2)

        # Do sides of rectangle
        x1 = start_x - offset
        x2 = start_x + offset
        for y in range(start_y - offset + 1, start_y + offset + 1 - 1):
            coord_count += check_coord(x1, y)
            coord_count += check_coord(x2, y)

        # Continue moving outward until we stop finding new coordinates
        if last_coord_count == coord_count:
            break
        last_coord_count = coord_count
        offset += 1

    return coord_count

answer = main()
print(f"Answer is {answer}")
