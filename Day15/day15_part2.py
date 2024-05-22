#!/usr/bin/python
"""Advent of Code 2018, Day 15, Part 2

https://adventofcode.com/2018/day/15

Given a map of elves and goblins, simulate a battle according to some
very fiddly rules to get right. In part2, we adjust the elves "power" until
they win without any losses.

See test*.dat for sample data and combat.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test1.dat'
fn = 'test2.dat'
fn = 'test3.dat'
fn = 'test4.dat'
fn = 'test5.dat'
fn = 'test8.dat'
fn = 'combat.dat'

import heapq
from collections import defaultdict, deque

max_dist = 999999

class Unit:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        self.hp = 200
        self.power = 3

    def __repr__(self):
        return f"[{self.type}: {(self.x, self.y)} ({self.hp})]"

    def copy(self):
        u = Unit(self.x, self.y, self.type)
        u.hp, u.power = self.hp, self.power
        return u

# Compute distances and paths to various end points using Dijkstra
def build_shortest_paths(grid, units, start):
    unit_set = set([ (u.x, u.y) for u in units ])

    # Dictionary to hold the shortest distances to each node
    distances = defaultdict(lambda: max_dist)

    # Priority queue to hold nodes to visit, starting with the start node
    priority_queue = [(0, start)]
    
    # Dictionary to hold the predecessors of each node
    predecessors = defaultdict(list)

    while priority_queue:
        # Get the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        # Process each neighbor of the current node
        x, y = current_node
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            x2, y2 = x+dx, y+dy
            if grid[y2][x2] != '.' or (x2, y2) in unit_set:
                continue

            neighbor = (x2, y2)
            distance = current_distance + 1

            # Only consider this new path if it's better than any path we've
            # previously found to the neighbor. Note we keep track of multiple
            # paths, so we can choose the right direction later in the combat.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                predecessors[neighbor] = [current_node]
            elif distance == distances[neighbor]:
                predecessors[neighbor].append(current_node)

    return distances, predecessors

# Extract list of first nodes for all shortest paths
def get_neighbors_in_path(start, end, predecessors):
    # This set will store the neighbors of the start node that are part of the shortest path to the end node
    neighbors_in_path = set()

    # Function to recursively trace paths back to the start node
    def trace_path(node):
        if node == start:
            return False
        for pred in predecessors[node]:
            if pred == start:  # If the predecessor of the current node is the start node
                neighbors_in_path.add(node)  # Add the current node (neighbor to start) to the set
            if trace_path(pred):  # Recursively trace back
                return True
        return False

    # Initialize tracing from the end node
    trace_path(end)

    return list(neighbors_in_path)

def dsp(grid, units):
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            unit = [ unit.type for unit in units if unit.x == x and unit.y == y ]
            if unit:
                print(unit[0], end='')
            else:
                print(c, end='')
        print()

def move_unit(grid, units, targets, unit):
    unit_set = set([ (u.x, u.y) for u in units ])

    # Step 2: For unit, identify list of points in range around each
    in_range = set()
    for other in targets:
        if other is not unit:
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                x2, y2 = other.x+dx, other.y+dy
                if grid[y2][x2] == '.' and (x2, y2) not in unit_set:
                    in_range.add((x2, y2))

    # Step 3: Figure out which are reachable
    reachable = []
    distances, predecessors = build_shortest_paths(grid, units, (unit.x, unit.y))
    for pair in in_range:
        d = distances[pair]
        if d != max_dist:
            reachable.append(pair)

    if len(reachable) == 0:
        return                    # Skip if no paths

    # Step 4: Figure out nearest reachable nodes
    min_len = min([ distances[r] for r in reachable ])
    nearest = [ r for r in reachable if distances[r] == min_len ]

    # Step 5: Choose destination in "reading order"
    nearest.sort(key=lambda item: (item[1], item[0]))
    dest = nearest[0]

    # Figure out first steps of paths to nearest and choose first in "reading order"
    first_step_list = get_neighbors_in_path((unit.x, unit.y), dest, predecessors)
    first_step_list.sort(key=lambda item: (item[1], item[0]))
    step = first_step_list[0]

    # Move the unit
    unit.x, unit.y = step[0], step[1]

def run_combat(grid, start_units):
    cycle = 0
    units = [ u.copy() for u in start_units ]

    while True:
        cycle += 1
        # Step 0: Order units top-to-bottom, left-to-right
        units.sort(key=lambda u: (u.y, u.x))

        for unit in units:
            if unit.hp <= 0:                # Skip newly dead units
                continue

            # Step 1: Identify enemy targets and see if any in range to attack
            enemy = 'G' if unit.type == 'E' else 'E'

            targets = { (u.x, u.y): u for u in units if u.type == enemy }
            if len(targets) == 0:
                return cycle-1, [ u for u in units if u.hp > 0 ]

            x, y = unit.x, unit.y
            attack_list = []
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                x2, y2 = unit.x+dx, unit.y+dy
                if (x2, y2) in targets:
                    attack_list.append(targets[x2, y2])

            # If no attack, process move
            if not attack_list:
                move_unit(grid, units, targets.values(), unit)

            # Check again for attacks
            x, y = unit.x, unit.y
            attack_list = []
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                x2, y2 = unit.x+dx, unit.y+dy
                if (x2, y2) in targets:
                    attack_list.append(targets[x2, y2])

            if attack_list:
                # Ready to attack
                low_hp = min(u.hp for u in attack_list)
                pot_list = [ u for u in attack_list if u.hp == low_hp ]
                pot_list.sort(key=lambda u: (u.y, u.x))
                attack = pot_list[0]
                attack.hp -= unit.power
                if attack.hp <= 0:          # Mark dead
                    attack.x, attack.y, attack.type = -1, -1, '-'+attack.type

        # Remove dead units
        units = [ u for u in units if u.hp > 0 ]

def main():
    grid = []
    start_units = []
    with open(fn, 'r') as file:
        for line in file:
            row, y = [], len(grid)
            for x, c in enumerate(line.rstrip("\n")):
                if c in ('G', 'E'):
                    start_units.append(Unit(x, y, c))
                    row += '.'
                else:
                    row += c
            grid.append(''.join(row))

    # Simulate combat with increasing elf power until no losses
    elf_power = 3
    final_e, start_e = 0, sum([ 1 for u in start_units if u.type == 'E' ])
    while start_e != final_e:
        elf_power += 1
        for u in ( u for u in start_units if u.type == 'E' ):
            u.power = elf_power

        num_cycles, units = run_combat(grid, start_units)
        final_e = sum([ 1 for u in units if u.type == 'E' ])
        print(f"Power: {elf_power}, E left: {final_e}, G left: {len(units) - final_e}")

    return num_cycles, units

num_cycles, units = main()
total = sum([ u.hp for u in units if u.hp > 0 ])
score = num_cycles * total
print(f"Answer is {score}, num_cycle = {num_cycles}, total was {total}")
