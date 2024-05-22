#!/usr/bin/python
"""Advent of Code 2018, Day 17, Part 1 and Part 2

https://adventofcode.com/2018/day/17

Given a list of clay tile coordinates, simulate water flowing down, filling
various capture points and overflowing.

See test.dat for sample data and clay.dat for full data.

Author: Tim Behrendsen
"""

import re

fn = 'test.dat'
fn = 'clay.dat'

max_y, min_y = 0, 999999
clay_tiles, path, filled = set(), set(), { }

def dsp():
    min_x = min(( t[0] for t in (clay_tiles | filled.keys() | path) ))
    max_x = max(( t[0] for t in (clay_tiles | filled.keys() | path) ))
    min_y = 0
    max_y = max(( t[1] for t in (clay_tiles | filled.keys() | path) ))
    for y in range(min_y, max_y+1):
        print(f"{y:4}: ", end='')
        for x in range(min_x, max_x+1):
            print(filled[(x, y)] if (x, y) in filled \
                else '|' if (x, y) in path \
                else '#' if (x, y) in clay_tiles \
                else '+' if (x, y) == (500, 0) \
                else '.', end='')
        print()

def fill_water(x, y):
    # Already processed this path?
    if (x, y) in path:
        return

    # Flow down until barrier or end
    while True:
        path.add((x, y))
        if (x, y+1) in clay_tiles:
            break
        y += 1
        if y > max_y:               # Bottom
            return

    # Hit barrier, spread to the sides, and rise if possible
    rise = True
    while rise:
        flow_list, hole_list = [ (x, y) ], [ ]
        for dir in (-1, 1):
            move_x = x
            while (move_x := move_x + dir, y) not in clay_tiles:
                flow_list.append((move_x, y))

                # If a hole, recursively check hole and mark no-rise for water
                is_filled = (move_x, y+1) in filled and filled[(move_x, y+1)] == '~'
                if not (move_x, y+1) in clay_tiles and not is_filled:
                    hole_list.append((move_x, y+1))
                    break

        y -= 1                      # If no holes, we'll rise up
        rise = len(hole_list) == 0
        for c in flow_list:         # Mark water as still or flowing
            filled[c] = '~' if rise else '^'

        for hole in hole_list:      # Recursively follow any holes
            fill_water(hole[0], hole[1])

def main():
    global clay_tiles, min_y, max_y

    with open(fn, 'r') as file:
        for line in file:
            a, b, c = map(int, re.findall(r'\d+', line))
            xr, yr = [(a, a), (b, c)] if line[0] == 'x' else [(b, c), (a, a)]
            for x in range(xr[0], xr[1]+1):
                for y in range(yr[0], yr[1]+1):
                    clay_tiles.add((x, y))
            max_y, min_y = max(max_y, yr[1]), min(min_y, yr[0])

    # Run simulation, part 1 and part 2 is just counting different ways
    fill_water(500, 0)
    #dsp()

    # Note need to count all coordinates with a 'y' within the original coordinates

    # Part 1: Total water
    n = len([ k for k in (filled.keys() | path) if k[1] >= min_y ])
    print(f"Part 1: {n}")

    # Part 2: Only standing water
    n = len([ k for k, c in filled.items() if k[1] >= min_y and c == '~' ])
    print(f"Part 2: {n}")

main()
