#!/usr/bin/python
"""Advent of Code 2018, Day 20, Part 1 and Part 2

https://adventofcode.com/2018/day/20

Given a "regular expression" that describes the cardinal directions possible in
a facility, figure out where the doors and walls are. Compute the distance to the
furthest point for Part 1, and calculate the number of rooms that are at least
1000 away in Part 2.

Tricky part is parsing the regex into a data structure. After that, building the
map and scanning are pretty straightforward. Uses Dijkstra to compute all the
distances.

Looking at other solutions on Reddit, looks like the problem was bounded enough
that a stack machine could have worked, but my solution is completely general and
will be efficient, even if there are multiple paths / loops.

See test.dat for sample data and regex.dat for full data.

Author: Tim Behrendsen
"""

import heapq
from collections import defaultdict

fn = 'test1.dat'
fn = 'test2.dat'
fn = 'test3.dat'
fn = 'test4.dat'
fn = 'regex.dat'

DSP = True

dirs = { 'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0) }
opp_dir = { 'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E' }

class Base:
    def __init__(self, p = None):
        self.list = [ ]
        if p != None:
            self.list.append(p)

    def append(self, p):
        self.list.append(p)

# Linear pattern -- must match in order
class Pattern(Base):
    def __repr__(self):
        return f"P:{self.list}"

# Alternating pattern -- can match from base point any of the list
class AltPattern(Base):
    def __repr__(self):
        return f"Alt:{self.list}"

# Token is string of cardinal directions
class Token:
    def __init__(self, c = None):
        self.s = ''
        if c != None:
            self.s += c
    def __iadd__(self, c):
        self.s += c
        return self
    def __repr__(self):
        return f"'{self.s}'"

# Trim pattern of extraneous empty strings that don't matter. Technically this
# isn't necessary and will work without it, but makes debugging easier.
def trim_pattern(pattern):
    if len(pattern.list) > 1:
        pattern.list = [ p for p in pattern.list \
            if not (p == ''
                or (type(p) in ('Pattern', 'AltPattern') and len(p.list) == 0)
                or (type(p) in ('Pattern', 'AltPattern') and len(p.list) == 1 and p.list[0] == '' )
                or (isinstance(p, Token) and p.s == ''))
            ]

# Parse the regex into a nested data structure
def parse(rx, pos):
    # The main loop accumulates a current linear pattern
    token = Token()
    pattern = Pattern()
    while pos < len(rx):
        c = rx[pos]
        if c in 'NSEW':
            token += c
        elif c == '(':
            # Start group, collect recursively
            pattern.append(token)
            token = Token()

            pos, sub_pattern = parse(rx, pos+1)
            pattern.append(sub_pattern)
        elif c == ')':
            # End of group
            pattern.append(token)
            trim_pattern(pattern)
            return pos, pattern
        elif c == '|':
            # Set up alt pattern and get each part recursively
            alt_pattern = AltPattern()
            pattern.append(token)
            trim_pattern(pattern)
            alt_pattern.append(pattern)
            pos, sub_pattern = parse(rx, pos+1)

            # Merge collected alternates into current alternate
            if isinstance(sub_pattern, AltPattern):
                alt_pattern.list += sub_pattern.list
            else:
                alt_pattern.list.append(sub_pattern)
            return pos, alt_pattern

        pos += 1

    pattern.append(token)
    trim_pattern(pattern)
    return pos, pattern

# Display the completed facility rooms and doors
def dsp(grid):
    min_x = min([k[0] for k in grid.keys()])
    max_x = max([k[0] for k in grid.keys()])
    min_y = min([k[1] for k in grid.keys()])
    max_y = max([k[1] for k in grid.keys()])
    num_x, num_y = max_x - min_x + 1, max_y - min_y + 1

    dsp_grid = [ ['?'] * (num_x*2+1) for y in range(num_y*2+1) ]
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            base_x = (x - min_x) * 2 + 1
            base_y = (y - min_y) * 2 + 1

            set_list = []
            set_list.append([base_y-1, base_x-1, '#' ])
            set_list.append([base_y-1, base_x, '-' if grid[(x, y)]['N'] == '*' else '#' ])
            set_list.append([base_y-1, base_x+1, '#' ])

            set_list.append([base_y, base_x-1, '|' if grid[(x, y)]['W'] == '*' else '#' ])
            set_list.append([base_y, base_x, 'X' if grid[(x, y)]['X'] else '.' ])
            set_list.append([base_y, base_x+1, '|' if grid[(x, y)]['E'] == '*' else '#' ])

            set_list.append([base_y+1, base_x-1, '#' ])
            set_list.append([base_y+1, base_x, '-' if grid[(x, y)]['S'] == '*' else '#' ])
            set_list.append([base_y+1, base_x+1, '#' ])
            for item in set_list:
                c = dsp_grid[item[0]][item[1]]
                if c != '?' and c != item[2]:           # Validate no contradictions
                    raise Exception("BAD")
                dsp_grid[item[0]][item[1]] = item[2]

    for row in dsp_grid:
        print(''.join(row))

# Find all unfilled directions and mark as walls
def fill_grid(grid):
    for node in grid.values():
        for d in 'NSEW':
            if node[d] == '?':
                node[d] = '#'

# Convert pattern to facility map
def make_grid(pattern):
    def recurse_pattern(grid, pattern, x, y):
        # Linear pattern, must match in order
        if isinstance(pattern, Pattern):
            work_x, work_y = x, y
            for p in pattern.list:
                work_x, work_y = recurse_pattern(grid, p, work_x, work_y)
            return work_x, work_y

        # Alternate paths pattern, any can match from base
        elif isinstance(pattern, AltPattern):
            for p in pattern.list:
                recurse_pattern(grid, p, x, y)
            return x, y

        # Token, follow the cardinal directions and set doors
        elif isinstance(pattern, Token):
            for d in pattern.s:
                grid[(x, y)][d] = '*'
                x, y = x + dirs[d][0], y + dirs[d][1]
                grid[(x, y)][opp_dir[d]] = '*'
            return x, y

    # Recursively follow pattern, filling in the doors
    grid = defaultdict(lambda: { 'N':'?', 'E':'?', 'S':'?', 'W':'?', 'X':False })
    grid[(0, 0)]['X'] = True
    recurse_pattern(grid, pattern, 0, 0)
    return grid

# Compute distances and paths to various end points using Dijkstra
def find_all_paths(grid, start):
    # Dictionary to hold the shortest distances to each node
    distances = defaultdict(lambda: 999999)
    pq = [(0, start)]
    
    while pq:
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(pq)
        if current_distance > distances[current_node]:
            continue                # See if stale (need for Python Dijkstra)

        # Process each neighbor of the current node
        x, y = current_node
        for d in 'NSEW':
            if grid[(x, y)][d] == '#':
                continue

            neighbor = (x+dirs[d][0], y+dirs[d][1])
            distance = current_distance + 1
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

def main():
    with open(fn, 'r') as file:
        regex = file.readline().rstrip("\n")

    _, pattern = parse(regex, 1)
    grid = make_grid(pattern)
    fill_grid(grid)

    if DSP:
        dsp(grid)
    distances = find_all_paths(grid, (0, 0))
    max_dist = max([ d for d in distances.values() ])
    print(f"Part 1: Maximum distance is {max_dist}")

    count = sum([ 1 for d in distances.values() if d >= 1000 ])
    print(f"Part 2: Number of paths at least 1000 doors is {count}")
    return

main()
