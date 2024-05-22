#!/usr/bin/python
"""Advent of Code 2018, Day 8, Part 2

https://adventofcode.com/2018/day/8

Given a tree data structure in a certain format, containing both sub-trees
and metadata values, sum up the "value" of the root node, which is the sum
of all the values of the child nodes. A node's value is either the sum of the
metadata values if no children, or the metadata indexes the list of children.

See test.dat for sample data and tree.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'tree.dat'

node_id = 0

def get_child(nums, idx=0):
    global node_id

    num_child, num_meta = nums[idx:idx+2]
    idx += 2
    children = []
    for i in range(num_child):
        idx, child = get_child(nums, idx)
        children.append(child)

    node = [ node_id := node_id+1, children, nums[idx:idx+num_meta] ]
    idx += num_meta
    return idx, node

def calc_value(node):
    # If no children, then value is sum of metadata. With children, add up values of
    # the children indexed by the metadata. Metadata indexes may be invalid.
    if len(node[1]) == 0:
        return sum(node[2])

    idx_list = [ n-1 for n in node[2] if n > 0 and n <= len(node[1]) ]
    return sum((calc_value(node[1][idx]) for idx in idx_list))

def main():
    with open(fn, 'r') as file:
        nums = [ int(n) for n in file.readline().split(' ') ]

    idx, node = get_child(nums)
    return calc_value(node)

answer = main()
print(f"Answer is {answer}")
