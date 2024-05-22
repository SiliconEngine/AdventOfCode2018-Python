#!/usr/bin/python
"""Advent of Code 2018, Day 4, Part 1

https://adventofcode.com/2018/day/4

Read log of a guard falling asleep and determine which guard was asleep the
most minutes. For that guard, determine which minute he was asleep the most.

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
    guard_total_sleep = { }
    guard_sleep_times = { }
    for line in log:
        matches = re.findall(r'\[(.*) (\d+):(\d+)\] (.*)', line)
        dt, h, m, desc = matches[0]

        if desc.startswith('Guard #'):
            cur_guard = int(re.findall(r'\d+', desc)[0])
            guard_total_sleep.setdefault(cur_guard, 0)
            guard_sleep_times.setdefault(cur_guard, [])

        elif desc == 'falls asleep':
            sleep_min = int(m)

        elif desc == 'wakes up':
            guard_total_sleep[cur_guard] += int(m) - sleep_min
            guard_sleep_times[cur_guard].append((sleep_min, int(m)))

    # Determine which guard was asleep the most
    most = -1
    most_g = -1
    for g, n in guard_total_sleep.items():
        if n > most:
            most = n
            most_g = g

    # Total of how many times asleep in that minute
    totals = [0] * 60
    for r in guard_sleep_times[most_g]:
        for m in range(r[0], r[1]):
            totals[m] += 1

    # Figure out which minute was most asleep
    most_tot = 0
    most_min = 0
    for i in range(60):
        if totals[i] > most_tot:
            most_min = i
            most_tot = totals[i]

    # Return product of guard number and minutes asleep
    return most_g * most_min

answer = main()
print(f"Answer is {answer}")
