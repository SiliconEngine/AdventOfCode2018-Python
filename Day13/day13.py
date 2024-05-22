#!/usr/bin/python
"""Advent of Code 2018, Day 13, Part 1 and Part 2

https://adventofcode.com/2018/day/13

Given carts on a track, simulate the carts traveling around the track and
predicting collisions.

See test.dat for sample data and track.dat for full data.

Author: Tim Behrendsen
"""

fn = 'test.dat'
fn = 'track.dat'

class Cart:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
        self.turn = 0
        self.stale = False

    def __repr__(self):
        return f"[{(self.x, self.y)}: {self.d} / {self.turn} / {self.stale}]"

moves = { '^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0), }

turns = {
    ('/', '^'): '>', ('/', 'v'): '<', ('/', '<'): 'v', ('/', '>'): '^',
    ('\\', '^'): '<', ('\\', 'v'): '>', ('\\', '<'): '^', ('\\', '>'): 'v',
}

rotate_l = { '^': '<', '<': 'v', 'v': '>', '>': '^' }
rotate_r = { '^': '>', '>': 'v', 'v': '<', '<': '^' }

tracks = []                 # Track map
carts = { }                 # List of carts, keyed by coordinates
with open(fn, 'r') as file:
    for line in file:
        new_line = []
        y = len(tracks)
        for x, c in enumerate(line.rstrip("\n")):
            if c in ('^', 'v', '<', '>'):
                carts[(x, y)] = Cart(x, y, c)
                c = '|' if c in ('^', 'v') else '-'
            new_line.append(c)
        tracks.append(''.join(new_line))

first = True
while True:
    # Create list that with proper order to process cart movement
    cart_list = sorted(carts.values(), key=lambda item: (item.y, item.x))
    if len(cart_list) == 1:
        break

    for cart in cart_list:
        if cart.stale:
            continue
        del carts[(cart.x, cart.y)]
        cart.x += moves[cart.d][0]
        cart.y += moves[cart.d][1]

        # See if colliding with another cart
        if (cart.x, cart.y) in carts:
            if first:
                print(f"Part 1: First collision is {(cart.x, cart.y)}")
                first = False
            # Remove carts from processing. Mark cart as stale, since it's still in cart_list
            carts[(cart.x, cart.y)].stale = True
            del carts[(cart.x, cart.y)]
        else:
            carts[(cart.x, cart.y)] = cart

        # Figure out if turning a new direction
        c = tracks[cart.y][cart.x]
        if c in ('/', '\\'):
            cart.d = turns[(c, cart.d)]
        elif c == '+':
            if cart.turn == 0:
                cart.d = rotate_l[cart.d]
            elif cart.turn == 2:
                cart.d = rotate_r[cart.d]
            cart.turn = (cart.turn+1) % 3

print(f"Part 2: final cart is {(cart_list[0].x, cart_list[0].y)}")
