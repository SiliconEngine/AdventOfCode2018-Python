#!/usr/bin/python
"""Advent of Code 2018, Day 16, Part 2

https://adventofcode.com/2018/day/16

Given a list of "samples" for output from a CPU's registers, figure out what
operation codes correspond to what functions using process of elimination.
Afterward, run the "test program" and return first register value.

See test.dat for sample data and tree.dat for full data.

Author: Tim Behrendsen
"""

import re
from collections import defaultdict

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

op_list = {
    'addr': addr, 'addi': addi, 'mulr': mulr, 'muli': muli, 
    'banr': banr, 'bani': bani, 'borr': borr, 'bori': bori, 
    'setr': setr, 'seti': seti, 'gtir': gtir, 'gtri': gtri, 
    'gtrr': gtrr, 'eqir': eqir, 'eqri': eqri, 'eqrr': eqrr }

def main():
    with open(fn, 'r') as file:
        # First read samples
        samples = []
        while True:
            line = file.readline().rstrip("\n")
            if line == '':          # Start of "test program"
                break
            before = [ int(n) for n in re.findall(r'\d+', line) ]
            op = [ int(n) for n in re.findall(r'\d+', file.readline().rstrip("\n")) ]
            after = [ int(n) for n in re.findall(r'\d+', file.readline().rstrip("\n")) ]
            file.readline()     # Blank line
            samples.append((op[0], op[1:4], before, after))

        # Read "test program"
        test_prog = []
        file.readline()     # Skip extra blank line
        while line := file.readline():
            op = [ int(n) for n in re.findall(r'\d+', line.rstrip("\n")) ]
            test_prog.append((op[0], op[1:4]))

    # Work out what op code does what. We'll mark a matrix when we find operations
    # that are impossible
    tracker = [ { code.__name__: True for code in op_list.values() } for i in range(16) ]
    for op, params, before, after in samples:
        for func in op_list.values():
            regs = before.copy()
            func(regs, params)
            if regs != after:
                tracker[op][func.__name__] = False

    # Resolve operations that can only be one
    checked = set()
    op_to_idx = { }
    while len(checked) < 16:
        counter = defaultdict(int)

        # Find functions that are True in only one op number
        for idx in range(16):
            for op, ok in tracker[idx].items():
                if op not in checked and ok:
                    counter[op] += 1
                    op_to_idx[op] = idx

        for op, count in counter.items():
            if op not in checked and count == 1:
                idx = op_to_idx[op]
                # Resolved idx to op, mark all the rest of the possibilities
                # in 'idx' to False
                for k in [ k for k in tracker[idx].keys() if k != op ]:
                    tracker[idx][k] = False

        # Find op numbers that only have one valid function
        for idx in range(16):
            op, count = '', 0
            for chk_op, flag in tracker[idx].items():
                if flag:
                    count += 1
                    op = chk_op
                if count > 1:
                    break

            if count == 1 and op not in checked:
                # Mark the function false in all the other numbers
                for i in [ i for i in range(16) if i != idx ]:
                    tracker[i][op] = False
                checked.add(op)

    idx_to_func = { idx: op for idx in range(16) for op, ok in tracker[idx].items() if ok }

    # Functions are resolved, run the final "test program"
    regs = [0, 0, 0, 0]
    for op, params in test_prog:
        func = op_list[idx_to_func[op]]
        func(regs, params)

    return regs[0]

answer = main()
print(f"Answer is {answer}")
