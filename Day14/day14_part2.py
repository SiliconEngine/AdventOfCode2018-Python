#!/usr/bin/python
"""Advent of Code 2018, Day 14, Part 2

https://adventofcode.com/2018/day/14

Given a cyclical recipe game, figure out when a sequence of scores appears.

See recipe.dat for full data.

Author: Tim Behrendsen
"""

fn = 'recipe.dat'

def main():
    with open(fn, 'r') as file:
        num = int(file.readline().rstrip("\n"))
    target = [ int(c) for c in str(num) ]

    scores = [ 3, 7 ]
    elf1, elf2 = 0, 1
    cycle = 0
    while True:
        if (cycle := cycle+1) % 1000000 == 0:
            print(cycle)
        last_len = len(scores)
        scores += [ int(c) for c in str(scores[elf1] + scores[elf2]) ]
        elf1 = (elf1 + scores[elf1] + 1) % len(scores)
        elf2 = (elf2 + scores[elf2] + 1) % len(scores)
        # Note that it's possible to get more than one number added to scores
        for idx in range(last_len+1, len(scores)+1):
            if scores[idx-len(target):idx] == target:
                return idx-len(target)

answer = main()
print(f"Answer is {answer}")
