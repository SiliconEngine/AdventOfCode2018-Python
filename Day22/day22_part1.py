#!/usr/bin/python
"""Advent of Code 2018, Day 22, Part 1

https://adventofcode.com/2018/day/22

Given an algorithm that determines a map of caves with certain
attributes, calculate the total of the attributes for a given region.

See test.dat for sample data and target.dat for full data.

Author: Tim Behrendsen
"""

import re

fn = 'test.dat'
fn = 'target.dat'

depth = 0
target = (0, 0)
grid_cache = { }

def get_region(x, y):
    if (x, y) in grid_cache: return grid_cache[(x, y)]
    elif (x, y) == (0, 0): geo_idx = 0
    elif (x, y) == target: geo_idx = 0
    elif y == 0: geo_idx = x * 16807
    elif x == 0: geo_idx = y * 48271
    else: geo_idx = get_region(x-1, y)[1] * get_region(x, y-1)[1]

    ero_level = (geo_idx + depth) % 20183
    grid_cache[(x, y)] = node = (geo_idx, ero_level, ero_level % 3)
    return node

def dsp(num_x, num_y):
    for y in range(num_y):
        for x in range(num_y):
            if (x, y) == (0, 0): c = 'M'
            elif (x, y) == target: c = 'T'
            else: c = ['.', '=', '|'][get_region(x, y)[2]]
            print(c, end='')
        print()

def main():
    global target, depth
    with open(fn, 'r') as file:
        depth = [ int(n) for n in re.findall(r'\d+', file.readline()) ][0]
        tx, ty = [ int(n) for n in re.findall(r'\d+', file.readline()) ]

    target = (tx, ty)
    risk_total = 0
    for y in range(ty+1):
        for x in range(tx+1):
            risk_total += get_region(x, y)[2]

    return risk_total

answer = main()
print(f"Answer is {answer}")
