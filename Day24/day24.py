#!/usr/bin/python
"""Advent of Code 2018, Day 24, Part 1 and Part 2

https://adventofcode.com/2018/day/24

Given a battle between an "infection" and an "immune system" that follows certain
rules, simulate the battle.
Part 1: Determine the outcome based on the input data.
Part 2: Calculate minimum boost to immune system to get a winning outcome.

See test.dat for sample data and condition.dat for full data.

Author: Tim Behrendsen
"""

import re, copy, itertools

fn = 'test.dat'
fn = 'condition.dat'

class Unit:
    def __init__(self, type, num_units, hit_points, attr_list, damage, attack_type, initiative):
        self.type = type
        self.num_units = int(num_units)
        self.hit_points = int(hit_points)
        self.attr_list = attr_list
        self.damage = int(damage)
        self.attack_type = attack_type
        self.initiative = int(initiative)

# Calculate effective power of unit
def calc_power(u):
    return u.num_units * u.damage

# Calculate damage to target
def calc_damage(attacker, target):
    for attr in target.attr_list:
        if attacker.attack_type in attr[1]:
            return 0 if attr[0] == 'immune' else calc_power(attacker)*2
    return calc_power(attacker)

def battle(base_units, boost=0):
    unit_list = [ copy.copy(u) for u in base_units ]
    for u in (u for u in unit_list if u.type == 'M'):
        u.damage += boost

    while True:
        # Select targets
        # Units choose in decreasing order of effective power, ties are by higher initiative
        attack_list, chosen = [], set()
        count = { 'M': 0, 'F': 0 }
        for attacker in sorted(unit_list, key=lambda u: (calc_power(u), u.initiative), reverse=True):
            if attacker.num_units == 0:
                continue
            count[attacker.type] += attacker.num_units
            targ_type = 'M' if attacker.type == 'F' else 'F'

            # Choose target with highest damage / power / initiative, in that order
            target, highest = None, (0, 0, 0)
            for t in (t for t in unit_list if t.type == targ_type and t.num_units != 0 and id(t) not in chosen):
                k = (calc_damage(attacker, t), calc_power(t), t.initiative)
                if k[0] > 0 and k > highest:
                    target, highest = t, k

            if target != None:
                chosen.add(id(target))
                attack_list.append((attacker, target))

        if count['M'] == 0 or count['F'] == 0:
            return count                # One of the armies lost

        # Execute the attack, in order of highest initiative first
        total_kills = 0
        for attacker, target in sorted(attack_list, key=lambda a: a[0].initiative, reverse=True):
            num_kill = min(calc_damage(attacker, target) // target.hit_points, target.num_units)
            target.num_units -= num_kill
            total_kills += num_kill

        if total_kills == 0:
            return None                 # No kills at all, so stalemate

type, unit_list = '', []
with open(fn, 'r') as file:
    for line in file:
        if line == '\n':
            continue
        if line[2:3] in ('m', 'f'):     # "Immune" or "Infect"
            type = line[2:3].upper()
            continue

        m = re.findall(r'(\d+) units each with (\d+) hit points (?:\((.*)\) )?with an attack that does (\d+) (\w+) damage at initiative (\d+)', line)
        num_units, hit_points, attrs, damage, attack_type, initiative = m[0]
        attr_list = []
        if attrs != '':
            for attr in attrs.split('; '):
                m = re.findall(r'(\w+) to (.*)', attr)[0]
                attr_list.append((m[0], m[1].split(', ')))

        unit_list.append(Unit(type, num_units, hit_points, attr_list, damage, attack_type, initiative))

result = battle(unit_list)
print(f"Part 1: {result['F']}")

for boost in itertools.count(1):
    result = battle(unit_list, boost=boost)
    if result != None and result['M'] != 0:
        break
print(f"Part 2: {result['M']}")
