#!/usr/bin/python
"""Advent of Code 2018, Day 11, Part 1

https://adventofcode.com/2018/day/11

Given a 300x300 grid that's filled in based on a formula, find the 3x3
grid with the highest total value. Uses a 1D partial sum.

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

    best_x, best_y, biggest = 0, 0, 0
    for y in range(1, 301-2):
        for x in range(1, 301-2):
            n = (grid[y][x+2] - grid[y][x-1]) + \
                (grid[y+1][x+2] - grid[y+1][x-1]) + \
                (grid[y+2][x+2] - grid[y+2][x-1])

            if n > biggest:
                best_x, best_y, biggest = x, y, n

    return (biggest, best_x, best_y)

answer = main()
print(f"Answer is {answer}")
