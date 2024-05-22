#!/usr/bin/python
"""Advent of Code 2018, Day 19, Part 2

https://adventofcode.com/2018/day/19

Given a program that runs on the CPU from day 16, run the program and
display what's on "register 0" when setting register 0 to 1.

This is impractically slow to run, so the puzzle required disassembling
what it actually did, which turned out to be the sum of the factors of a
number that it calculates internally.

See test.dat for sample data and program.dat for full data.

Author: Tim Behrendsen
"""

def main():
    part1_target = 1003
    part2_target = 10551403

    # Fast mode, sum the factors of the number.
    def get_factors(num):
        factors = []
        for i in range(1, int(num ** .5) + 1):
            if num % i == 0:
                factors.append(i)
                if i != num // i:
                    factors.append(num // i)
        return sorted(factors)

    print(f"Part 1: {sum(get_factors(part1_target))}")
    print(f"Part 2: {sum(get_factors(part2_target))}")
    exit(0)

    # Converted to Python loops
    # Two loops that add the loop value when they multiply together to produce
    # the target, which will hit when we have factors of the number. Bottom line
    # is that it's the sum of the factors of the number

    part = 1 # 2
    counter1, counter2, total, scratch, target = 0, 0, 0, 0, 0
    target = part1_target if part == 1 else part2_target
    counter1 = 1
    while counter1 <= target:
        counter2 = 1
        while counter2 <= target:
            if (counter1 * counter2) == target:
                total += counter1

            counter2 += 1
        counter1 += 1

    print(f"total = {total}")           # 0
    print(f"[not used]")                # 1
    print(f"target = {target}")         # 2
    print(f"counter1 = {counter1}")     # 3
    print(f"scratch = {scratch}")       # 4
    print(f"counter2 = {counter2}")     # 5
    exit(0)

    # Boiled down program instructions
    regs = [0, 0, 0, 0, 0, 0]
    ip = 0
    counter1, counter2, total, scratch, target = 0, 0, 0, 0, 0

    def set_ip(new_ip):
        nonlocal ip
        #print(f"IP set to {new_ip}, was {ip}")
        ip = new_ip

    while ip < 36:
        save_ip = ip
        if ip == 1: #  seti 1 5 3
            counter1 = 1

        elif ip == 2: #  seti 1 7 5
            counter2 = 1

        elif ip == 3: #  mulr 3 5 4
            if (counter1 * counter2) == target:
                total += counter1

            counter2 += 1
            if counter2 > target:
                #set_ip(12)
                counter1 += 1
                scratch = counter1 > target
                if counter1 > target:
                    break
                set_ip(2)
                continue

            set_ip(3)
            continue

        else:
            print(f"BAD {ip}, last was {last_ip}, save is {save_ip}")
            exit(0)

        last_ip = save_ip
        ip += 1

    print(f"total = {total}")           # 0
    print(f"[not used]")                # 1
    print(f"target = {target}")         # 2
    print(f"counter1 = {counter1}")     # 3
    print(f"scratch = {scratch}")       # 4
    print(f"counter2 = {counter2}")     # 5
    print(regs)

main()
