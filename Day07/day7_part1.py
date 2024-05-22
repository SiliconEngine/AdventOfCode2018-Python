#!/usr/bin/python
"""Advent of Code 2018, Day 7, Part 1

https://adventofcode.com/2018/day/7

Given a series of steps with prerequisites, figure out the order of the steps.

See test.dat for sample data and steps.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'steps.dat'

import re
from collections import defaultdict

def main():
    rules = defaultdict(list)
    all_steps = set()
    with open(fn, 'r') as file:
        for line in file:
            # Step C must be finished before step A can begin.
            m = re.findall(r'Step (.).*step (.)', line)[0]
            # key depends on value
            rules[m[1]].append(m[0])
            all_steps.update([ m[0], m[1] ])

    completed = set()
    order = []
    while True:
        not_ready = set()
        #for step, must_have in rules.items():
        for step in all_steps:
            for must_have in rules[step]:
                if must_have not in completed:
                    not_ready.add(step)

        chk = [ step for step in all_steps if step not in not_ready and step not in completed ]
        chk.sort()
        completed.add(chk[0])
        order.append(chk[0])
        if len(completed) == len(all_steps):
            break

    return ''.join(order)

answer = main()
print(f"Answer is {answer}")
