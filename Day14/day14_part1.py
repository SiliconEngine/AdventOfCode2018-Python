#!/usr/bin/python
"""Advent of Code 2018, Day 14, Part 1

https://adventofcode.com/2018/day/14

Given a cyclical recipe game, figure out the 10 scores after the number of
target cycles.

See recipe.dat for full data.

Author: Tim Behrendsen
"""

fn = 'recipe.dat'

def main():
    with open(fn, 'r') as file:
        target = int(file.readline().rstrip("\n"))

    scores = [ 3, 7 ]
    elf1, elf2 = 0, 1
    limit = 10 + target
    while (limit := limit-1):
        scores += [ int(c) for c in str(scores[elf1] + scores[elf2]) ]
        elf1 = (elf1 + scores[elf1] + 1) % len(scores)
        elf2 = (elf2 + scores[elf2] + 1) % len(scores)

    return ''.join([ str(n) for n in scores[target:target+10] ])

answer = main()
print(f"Answer is {answer}")
