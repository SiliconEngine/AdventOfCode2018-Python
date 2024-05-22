#!/usr/bin/python
"""Advent of Code 2018, Day 25

https://adventofcode.com/2018/day/25

Given a list of four-dimensional stars, calculate number of "constellations"
where the stars are within 3 units of each other (manhattan distance)

See test.dat for sample data and stars.dat for full data.

Author: Tim Behrendsen
"""

from collections import defaultdict

fn = 'test.dat'
fn = 'test2.dat'
fn = 'stars.dat'

def dist(s1, s2):
    return abs(s1[0]-s2[0]) + abs(s1[1]-s2[1]) + abs(s1[2]-s2[2]) + abs(s1[3]-s2[3])

with open(fn, 'r') as file:
    stars = [ [ int(n) for n in line.rstrip('\n').split(',') ] for line in file ]

# Build graph of stars next to each other
graph = defaultdict(list)
for i1 in range(len(stars)):
    for i2 in range(i1+1, len(stars)):
        if dist(stars[i1], stars[i2]) <= 3:
            graph[i1].append(i2)
            graph[i2].append(i1)

# Recursively follow each un-visited star and count
seen = set()
def follow(idx):
    if idx not in seen:
        seen.add(idx)
        for i in graph[idx]: follow(i)

count = 0
for idx in range(len(stars)):
    if idx not in seen:
        count += 1
        follow(idx)

print(f"Number of constellations is {count}")
