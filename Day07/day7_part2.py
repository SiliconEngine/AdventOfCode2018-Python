#!/usr/bin/python
"""Advent of Code 2018, Day 7, Part 2

https://adventofcode.com/2018/day/7

Given a series of steps with prerequisites, figure out how long the steps
take to complete given five parallel workers.

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
            # "Step C must be finished before step A can begin."
            m = re.findall(r'Step (.).*step (.)', line)[0]
            rules[m[1]].append(m[0])            # key depends on values
            all_steps.update([ m[0], m[1] ])

    completed = set()
    workers = [ [ '', 0 ], [ '', 0 ], [ '', 0 ], [ '', 0 ], [ '', 0 ] ]
    total_time = 0
    while True:
        # Figure how much time to move and move the clock
        move_time = min([ t for letter, t in workers if t > 0 ], default=0)
        total_time += move_time
        for wrk in (w for w in workers if w[0] != '' and w[1] > 0):
            wrk[1] -= move_time
            if wrk[1] == 0:
                completed.add(wrk[0])

        if len(completed) == len(all_steps):
            break

        # Figure out next to move
        not_ready = set(( w[0] for w in workers if w[0] != '' ))
        for step in all_steps:
            for must_have in rules[step]:
                if must_have not in completed:
                    not_ready.add(step)
        ready = sorted([ step for step in all_steps if step not in not_ready and step not in completed ])

        # Assign workers
        wlist = [ i for i, w in enumerate(workers) if w[1] == 0 ]
        while ready and wlist:
            workers[wlist[0]] = [ ready[0], 61 + ord(ready[0]) - ord('A') ]
            ready.pop(0)
            wlist.pop(0)

    return total_time

answer = main()
print(f"Answer is {answer}")
