#!/usr/bin/python
"""Advent of Code 2018, Day 11, Part 2

https://adventofcode.com/2018/day/11

Given a 300x300 grid that's filled in based on a formula, find the NxN
square with the highest total value. Uses a 1D partial sum, which isn't
super fast, and this could be improved by going to a 2D partial sum.

Author: Tim Behrendsen
"""

def main():
    sn = 6392

    def calc_power(x, y):
        rack_id = x + 10
        power = rack_id * y
        power += sn
        power *= rack_id
        power = (power // 100) % 10
        power -= 5
        return power

    grid = [[0 for _ in range(301)] for _ in range(301)]
    for y in range(1, 301):
        for x in range(1, 301):
            grid[y][x] = calc_power(x, y) + grid[y][x-1]

    size = 300
    best_x, best_y, best_s, biggest = 0, 0, 0, 0
    for y in range(1, size+1):
        print((y, biggest))
        for x in range(1, size+1):
            for s in range(1, size-max(x, y)+2):
                n = 0
                for idx in range(s):
                    r = grid[y+idx]
                    n += r[x+s-1] - r[x-1]

                if n > biggest:
                    best_x, best_y, best_s = x, y, s
                    biggest = n

    return (biggest, best_x, best_y, best_s)

answer = main()
print(f"Answer is {answer}")
