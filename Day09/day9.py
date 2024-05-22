#!/usr/bin/python
"""Advent of Code 2018, Day 9, Part 1 and Part 2

https://adventofcode.com/2018/day/9

Simulate a marble game played in a circle, inserting and deleting marbles
at various positions and adding up a score. Display the highest score at
the end. The puzzle instructions are unclear about when to stop, but you run
until the given final marble number.

See test.dat for sample data and game.dat for full data.

Author: Tim Behrendsen
"""

import re
from collections import deque

fn = 'test.dat'
fn = 'game.dat'

def run_game(players, last_marb):
    scores = [0] * players
    circle = deque([0])
    next_marble, player = 0, 0
    while (next_marble := next_marble+1) != last_marb:
        if (next_marble % 23) == 0:
            circle.rotate(7)
            scores[player] += circle.popleft() + next_marble
        else:
            circle.rotate(-2)
            circle.appendleft(next_marble)

        player = (player+1) % players

    return max(scores)

with open(fn, 'r') as file:
    players, last_marb = [ int(n) for n in re.findall(r'\d+', file.readline()) ]

print(f"Part 1: {run_game(players, last_marb)}")
print(f"Part 2: {run_game(players, last_marb * 100)}")
