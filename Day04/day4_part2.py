#!/usr/bin/python
"""Advent of Code 2018, Day 4, Part 2

https://adventofcode.com/2018/day/4

Read log of a guard falling asleep and determine which guard was asleep the most
in a particular minute.

See test.dat for sample data and guards.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'guards.dat'

import re

def main():
    log = []
    with open(fn, 'r') as file:
        log = [ line.rstrip("\n") for line in file ]

    log.sort()
    cur_guard = None
    sleep_min = None
    guard_sleep_times = { }
    for line in log:
        matches = re.findall(r'\[(.*) (\d+):(\d+)\] (.*)', line)
        dt, h, m, desc = matches[0]

        if desc.startswith('Guard #'):
            cur_guard = int(re.findall(r'\d+', desc)[0])
            guard_sleep_times.setdefault(cur_guard, [])

        elif desc == 'falls asleep':
            sleep_min = int(m)

        elif desc == 'wakes up':
            guard_sleep_times[cur_guard].append((sleep_min, int(m)))

    # For each guard, figure out how much asleep in each minute
    most_g = -1
    most_tot = -1
    most_min = -1
    for g in guard_sleep_times.keys():
        # Accumulate total for guard
        totals = [0] * 60
        for r in guard_sleep_times[g]:
            for m in range(r[0], r[1]):
                totals[m] += 1

        # See if guard beats the record of most minutes
        for i in range(60):
            if totals[i] > most_tot:
                most_min = i
                most_tot = totals[i]
                most_g = g

    return most_g * most_min

answer = main()
print(f"Answer is {answer}")
