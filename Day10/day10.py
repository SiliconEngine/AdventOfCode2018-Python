#!/usr/bin/python
"""Advent of Code 2018, Day 10, Part 1 and Part 2

https://adventofcode.com/2018/day/10

Given a "star map" with coordinates and velocities, figure out what
message they eventually spell out after all the movement.

See test.dat for sample data and points.dat for full data.

Author: Tim Behrendsen
"""

import re

fn = 'test.dat'
fn = 'points.dat'

def dsp(points):
    min_x, max_x = min(( p[0] for p in points )), max(( p[0] for p in points ))
    min_y, max_y = min(( p[1] for p in points )), max(( p[1] for p in points ))
    pts = set([ (p[0], p[1]) for p in points ])
    for y in range(min_y, max_y+1):
        print(''.join([ '#' if (x, y) in pts else '.' for x in range(min_x, max_x+1) ]))

with open(fn, 'r') as file:
    points = [ [ int(n) for n in re.findall(r'[\-\d]+', line) ] for line in file ]

last_range_x, last_range_y = 9999999, 9999999
loop = 0
while True:
    loop += 1
    for w in points:
        w[0] += w[2]
        w[1] += w[3]

    # Look for when coordinates converge and then start spreading again
    min_x, max_x = min(( p[0] for p in points )), max(( p[0] for p in points ))
    min_y, max_y = min(( p[1] for p in points )), max(( p[1] for p in points ))
    range_x, range_y = max_x-min_x, max_y-min_y
    if range_x > last_range_x or range_y > last_range_y:
        break

    last_range_x, last_range_y = range_x, range_y

# Started getting bigger, reverse the current step
for w in points:
    w[0] -= w[2]
    w[1] -= w[3]

print("PART 1")
dsp(points)
print(f"Part 2: {loop-1}")
