#!/usr/bin/python
"""Advent of Code 2018, Day 8, Part 1

https://adventofcode.com/2018/day/8

Given a tree data structure in a certain format, containing both sub-trees
and metadata values, create the tree and sum up the metadata.

See test.dat for sample data and tree.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'tree.dat'

node_id = 0
meta_total = 0

# Build the tree and sum up the metadata values
def get_child(nums, idx=0):
    global node_id, meta_total
    num_child, num_meta = nums[idx:idx+2]

    idx += 2
    children = []
    for i in range(num_child):
        idx, child = get_child(nums, idx)
        children.append(child)

    node = [ node_id := node_id+1, children, nums[idx:idx+num_meta] ]
    idx += num_meta
    meta_total += sum(node[2])
    return idx, node

def main():
    with open(fn, 'r') as file:
        nums = [ int(n) for n in file.readline().split(' ') ]

    idx, node = get_child(nums)
    return meta_total

answer = main()
print(f"Answer is {answer}")
