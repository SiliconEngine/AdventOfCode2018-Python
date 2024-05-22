#!/usr/bin/python
"""Advent of Code 2018, Day 16, Part 1

https://adventofcode.com/2018/day/16

Given a list of "samples" for output from a CPU's registers, figure out what
operation codes are possible, and compute how many have more than three
possibilities.

See test.dat for sample data and tree.dat for full data.

Author: Tim Behrendsen
"""

import re

fn = 'test.dat'
fn = 'samples.dat'

def addr(regs, params):
    regs[params[2]] = regs[params[0]] + regs[params[1]]

def addi(regs, params):
    regs[params[2]] = regs[params[0]] + params[1]

def mulr(regs, params):
    regs[params[2]] = regs[params[0]] * regs[params[1]]

def muli(regs, params):
    regs[params[2]] = regs[params[0]] * params[1]

def banr(regs, params):
    regs[params[2]] = regs[params[0]] & regs[params[1]]

def bani(regs, params):
    regs[params[2]] = regs[params[0]] & params[1]

def borr(regs, params):
    regs[params[2]] = regs[params[0]] | regs[params[1]]

def bori(regs, params):
    regs[params[2]] = regs[params[0]] | params[1]

def setr(regs, params):
    regs[params[2]] = regs[params[0]]

def seti(regs, params):
    regs[params[2]] = params[0]

def gtir(regs, params):
    regs[params[2]] = 1 if params[0] > regs[params[1]] else 0

def gtri(regs, params):
    regs[params[2]] = 1 if regs[params[0]] > params[1] else 0

def gtrr(regs, params):
    regs[params[2]] = 1 if regs[params[0]] > regs[params[1]] else 0

def eqir(regs, params):
    regs[params[2]] = 1 if params[0] == regs[params[1]] else 0

def eqri(regs, params):
    regs[params[2]] = 1 if regs[params[0]] == params[1] else 0

def eqrr(regs, params):
    regs[params[2]] = 1 if regs[params[0]] == regs[params[1]] else 0

op_list = [ addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtir, gtrr, eqir, eqir, eqrr ]

def main():
    with open(fn, 'r') as file:
        samples = []
        while True:
            line = file.readline().rstrip("\n")
            if line == '':          # Start of "test program", which is skipped in part 1
                break
            before = [ int(n) for n in re.findall(r'\d+', line) ]
            op = [ int(n) for n in re.findall(r'\d+', file.readline().rstrip("\n")) ]
            after = [ int(n) for n in re.findall(r'\d+', file.readline().rstrip("\n")) ]
            file.readline()     # Blank line
            samples.append((op[0], op[1:4], before, after))

    total_count = 0
    for op, params, before, after in samples:
        match_count = 0
        for func in op_list:
            regs = before.copy()
            func(regs, params)
            if regs == after:
                match_count += 1

        if match_count >= 3:
            total_count += 1

    return total_count

answer = main()
print(f"Answer is {answer}")
