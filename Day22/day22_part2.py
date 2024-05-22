#!/usr/bin/python
"""Advent of Code 2018, Day 22, Part 2

https://adventofcode.com/2018/day/22

Given an algorithm that determines a map of caves with certain attributes, and
rules about how the cave system can be followed, calculate the shortest path.

See test.dat for sample data and target.dat for full data.

Author: Tim Behrendsen
"""

import re
import heapq
from collections import defaultdict, deque

fn = 'test.dat'
fn = 'target.dat'

symbols = [ '.', '=', '|' ]
depth = 0
target = (0, 0)
grid_cache = { }

# Tools needed for each region type. Gear is 'N', 'C' or 'T'
needs = {
    '.': ( 'C', 'T' ),
    '=': ( 'C', 'N' ),
    '|': ( 'T', 'N' ),
}

# Get info at a node.
def get_region(x, y):
    if (x, y) in grid_cache: return grid_cache[(x, y)]
    elif (x, y) == (0, 0): geo_idx = 0
    elif (x, y) == target: geo_idx = 0
    elif y == 0: geo_idx = x * 16807
    elif x == 0: geo_idx = y * 48271
    else: geo_idx = get_region(x-1, y)[1] * get_region(x, y-1)[1]

    ero_level = (geo_idx + depth) % 20183
    grid_cache[(x, y)] = node = (geo_idx, ero_level, symbols[ero_level % 3])
    return node

# Display the region map
def dsp(num_x, num_y):
    for y in range(num_y):
        for x in range(num_y):
            if (x, y) == (0, 0): c = 'M'
            elif (x, y) == target: c = 'T'
            else: c = get_region(x, y)[2]
            print(c, end='')
        print()

# Compute distance to end using Dijkstra
def find_path(start, end):
    # Dictionary to hold the shortest distances to each node. Each node
    # is (x, y, gear).
    distances = defaultdict(lambda: 999999)
    pq = [(0, (start[0], start[1], 'T'))]       # Note starting with torch

    while pq:
        # Get the node with the smallest distance
        cur_dist, cur_node = heapq.heappop(pq)
        if cur_dist > distances[cur_node]:
            continue                # See if stale (need for Python Dijkstra)

        # See if found end, note that needs to end on torch
        if (cur_node[0], cur_node[1]) == end and cur_node[2] == 'T':
            return cur_dist

        x, y, cur_gear = cur_node
        cur_needs = needs[get_region(x, y)[2]]
        other_gear = cur_needs[0] if cur_gear == cur_needs[1] else cur_needs[1]
        new_q = []

        # Add node for switching gear at current point
        new_q.append((cur_dist + 7, (x, y, other_gear)))

        # See what movements are valid
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x+dx, y+dy
            if nx < 0 or ny < 0:
                continue
            new_reg = get_region(nx, ny)

            # Add if our current gear is valid for moving to this location
            if cur_gear in needs[new_reg[2]]:
                node = (nx, ny, cur_gear)
                new_q.append((cur_dist + 1, (nx, ny, cur_gear)))

        # Add the valid neighbor nodes
        for distance, node in new_q:
            if distance < distances[node]:
                distances[node] = distance
                heapq.heappush(pq, (distance, node))

    return None

def main():
    global target, depth
    with open(fn, 'r') as file:
        depth = [ int(n) for n in re.findall(r'\d+', file.readline()) ][0]
        tx, ty = [ int(n) for n in re.findall(r'\d+', file.readline()) ]

    target = (tx, ty)
    return find_path((0, 0), target)

answer = main()
print(f"Answer is {answer}")
