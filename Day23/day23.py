#!/usr/bin/python
"""Advent of Code 2018, Day 23, Part 1 and Part 2

https://adventofcode.com/2018/day/23

Given a set of "bot" coordinates and a scanning manhattan-distance radius, figure out:
Part 1: How many bots in range of the bot with the largest radius.
Part 2: What position is in range of the most bots and closest to 0,0,0 origin.

Part 2 is tricky and requires dividing a bounding cuboid into smaller and smaller
regions, and keeping a priority queue to hone in on the best coordinate.

See test.dat for sample data and bots.dat for full data.

Author: Tim Behrendsen
"""

import re, sys, heapq

fn = 'test.dat'
fn = 'test2.dat'
fn = 'bots.dat'

# Check if bot is contained in cubic area
def bot_in_cube(bot, cube):
    def in_cube(vtx, cube):
        return cube[0] <= vtx[0] <= cube[1] and cube[2] <= vtx[1] <= cube[3] and cube[4] <= vtx[2] <= cube[5]
    def in_bot(vtx, bot):
        return abs(vtx[0] - bot[0]) + abs(vtx[1] - bot[1]) + abs(vtx[2] - bot[2]) <= bot[3]

    # First check if bot vertexes contained in cube
    x, y, z, r = bot
    for vtx in ((x-r, y, z), (x+r, y, z), (x, y-r, z), (x, y+r, z), (x, y, z-r), (x, y, z+r)):
        if in_cube(vtx, cube): return True

    # Check if cube vertexes contained in bot region
    x1, x2, y1, y2, z1, z2 = cube
    for vtx in ((x1, y1, z1), (x2, y1, z1), (x1, y2, z1), (x2, y2, z1), \
            (x1, y1, z2), (x2, y1, z2), (x1, y2, z2), (x2, y2, z2)):
        if in_bot(vtx, bot): return True

    return False

# Get nearest distance to origin for cube area
def get_origin_dist(cube):
    x1, x2, y1, y2, z1, z2 = cube
    cube_vtx = ( (x1, y1, z1), (x2, y1, z1), (x1, y2, z1), (x2, y2, z1),
        (x1, y1, z2), (x2, y1, z2), (x1, y2, z2), (x2, y2, z2))
    return min([ abs(vtx[0])+abs(vtx[1])+abs(vtx[2]) for vtx in cube_vtx ])

# Get volume of cube
def get_volume(cube):
    x1, x2, y1, y2, z1, z2 = cube
    return (abs(x2-x1)+1) * (abs(y2-y1)+1) * (abs(z2-z1)+1)

# Calculate part 2 (nearest point to origin within most bots)
def part2(bots):
    min_x, min_y, min_z = sys.maxsize, sys.maxsize, sys.maxsize
    max_x, max_y, max_z = -sys.maxsize, -sys.maxsize, -sys.maxsize

    for b in bots:
        x, y, z, r = b
        min_x, min_y, min_z = min(min_x, x-r), min(min_y, y-r), min(min_z, z-r)
        max_x, max_y, max_z = max(max_x, x+r), max(max_y, y+r), max(max_z, z+r)

    # Set up priority queue of cuboids: #bots, volume, dist from origin, cuboid
    # We do the volume so it divides the largest areas first
    start_cube = (min_x, max_x, min_y, max_y, min_z, max_z)
    pq = [ (-len(bots), -get_volume(start_cube), get_origin_dist(start_cube), start_cube) ]
    seen = set()
    best_count, best_dist = 0, 0
    while len(pq):
        cur_count, cur_volume, cur_dist, (x1, x2, y1, y2, z1, z2) = heapq.heappop(pq)

        # If node is already worse than our best count, skip
        if (0-cur_count) < best_count:
            continue

        # Divide node cuboid into half cuboids
        xgt1, ygt1, zgt1 = x1 != x2, y1 != y2, z1 != z2
        half_x, half_y, half_z = (x1+x2) // 2, (y1+y2) // 2, (z1+z2) // 2
        cubes = [ (x1, half_x, y1, half_y, z1, half_z) ]
        if xgt1:
            cubes.append((half_x+1, x2, y1, half_y, z1, half_z))
            if ygt1:
                cubes.append((half_x+1, x2, half_y+1, y2, z1, half_z))
                if zgt1:
                    cubes.append((half_x+1, x2, half_y+1, y2, half_z+1, z2))
        if ygt1:
            cubes.append((x1, half_x, half_y+1, y2, z1, half_z))
            if zgt1:
                cubes.append((x1, half_x, half_y+1, y2, half_z+1, z2))
        if zgt1:
            cubes.append((x1, half_x, y1, half_y, half_z+1, z2))
            if xgt1:
                cubes.append((half_x+1, x2, y1, half_y, half_z+1, z2))

        # Check if each cube may contain more bots
        for c in cubes:
            bot_count = sum((1 for b in bots if bot_in_cube(b, c)))
            origin_dist, volume = get_origin_dist(c), get_volume(c)
            if c not in seen:       # Only add if not been seen before
                heapq.heappush(pq, (-bot_count, -volume, origin_dist, c))
                seen.add(c)

            # If a single region, check if it's best so far
            if volume == 1:
                if bot_count > best_count:
                    best_count = bot_count
                    best_dist = origin_dist
                elif bot_count == best_count and origin_dist < best_dist:
                    best_dist = origin_dist

    return best_dist

# Part 1: Calculate the number of bots in range of the bot with the largest radius
def part1(bots):
    def calc_dist(b1, b2): return abs(b1[0]-b2[0]) + abs(b1[1]-b2[1]) + abs(b1[2]-b2[2])

    br, biggest = max([ (b[3], b) for b in bots ])
    return sum([ 1 for bot in bots if calc_dist(bot, biggest) < biggest[3] ])

# Main
bots = []
with open(fn, 'r') as file:
    for line in file:
        nums = [ int(n) for n in re.findall(r'[-\d]+', line) ]
        bots.append(tuple(nums))

print(f"Part 1: {part1(bots)}")
print(f"Part 2: {part2(bots)}")
