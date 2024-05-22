# Advent of Code 2018 solutions written in Python.
## Author: Tim Behrendsen

Link: https://adventofcode.com/2018/

Advent of Code is a series of puzzles over 25 days, each with a part 1 and
part 2. The difficulty roughly rises each day, with the later puzzles often
requiring some tricky algorithms to solve.

For these solutions, the various days are in separate directories, with a
separate file for each part. Day 25, as traditional, is only a single part.

### Advent of Code 2018, Day 1, Part 1

Link: https://adventofcode.com/2018/day/1

Given a list of "changes in frequency", calculate the sum total.

### Advent of Code 2018, Day 1, Part 2

Link: https://adventofcode.com/2018/day/1

Given a list of "changes in frequency", calculate the sum total, and find
the first frequence that repeats after cycling the list in a loop

### Advent of Code 2018, Day 2, Part 1

Link: https://adventofcode.com/2018/day/2

For list of box IDs, figure out which ones have exactly two of the same
letter and three of the same letter.

### Advent of Code 2018, Day 2, Part 2

Link: https://adventofcode.com/2018/day/2

For list of boxes, figure out what pair have exactly one letter difference, then
output common letters between those two.

### Advent of Code 2018, Day 3, Part 1

Link: https://adventofcode.com/2018/day/3

Given a list of "claims", which are coordinates of a rectangle within a
1000x1000 sheet of cloth, figure out how many squares overlap.

### Advent of Code 2018, Day 3, Part 2

Link: https://adventofcode.com/2018/day/3

Given a list of "claims", which are coordinates of a rectangle within a
1000x1000 sheet of cloth, figure out which one doesn't overlap any of them.

### Advent of Code 2018, Day 4, Part 1

Link: https://adventofcode.com/2018/day/4

Read log of a guard falling asleep and determine which guard was asleep the
most minutes. For that guard, determine which minute he was asleep the most.

### Advent of Code 2018, Day 4, Part 2

Link: https://adventofcode.com/2018/day/4

Read log of a guard falling asleep and determine which guard was asleep the most
in a particular minute.

### Advent of Code 2018, Day 5, Part 1

Link: https://adventofcode.com/2018/day/5

Given a list of letters that make up a "polymer", eliminate sets of letters
that pair with opposite case (reacting and destroying themselves).

### Advent of Code 2019, Day 5, Part 2

Link: https://adventofcode.com/2019/day/5

Given a list of letters that make up a "polymer", eliminate sets of letters
that pair with opposite case (reacting and destroying themselves). For Part 2,
remove a letter and figure out which removal results in the smallest polymer
after reduction.

### Advent of Code 2018, Day 6, Part 1

Link: https://adventofcode.com/2018/day/6

Given a list of coordinates, figure out the size of the largest area that
is furthest away from all points (manhattan distance), while being within
the coordinates.

### Advent of Code 2018, Day 6, Part 2

Link: https://adventofcode.com/2018/day/5

Given a list of coordinates, figure out the number of coordinates where the total of
the manhattan distance to all given coordinates is < 10000.

### Advent of Code 2018, Day 7, Part 1

Link: https://adventofcode.com/2018/day/7

Given a series of steps with prerequisites, figure out the order of the steps.

### Advent of Code 2018, Day 7, Part 2

Link: https://adventofcode.com/2018/day/7

Given a series of steps with prerequisites, figure out how long the steps
take to complete given five parallel workers.

### Advent of Code 2018, Day 8, Part 1

Link: https://adventofcode.com/2018/day/8

Given a tree data structure in a certain format, containing both sub-trees
and metadata values, create the tree and sum up the metadata.

### Advent of Code 2018, Day 8, Part 2

Link: https://adventofcode.com/2018/day/8

Given a tree data structure in a certain format, containing both sub-trees
and metadata values, sum up the "value" of the root node, which is the sum
of all the values of the child nodes. A node's value is either the sum of the
metadata values if no children, or the metadata indexes the list of children.

### Advent of Code 2018, Day 9, Part 1 and Part 2

Link: https://adventofcode.com/2018/day/9

Simulate a marble game played in a circle, inserting and deleting marbles
at various positions and adding up a score. Display the highest score at
the end. The puzzle instructions are unclear about when to stop, but you run
until the given final marble number.

### Advent of Code 2018, Day 10, Part 1 and Part 2

Link: https://adventofcode.com/2018/day/10

Given a "star map" with coordinates and velocities, figure out what
message they eventually spell out after all the movement.

### Advent of Code 2018, Day 11, Part 1

Link: https://adventofcode.com/2018/day/11

Given a 300x300 grid that's filled in based on a formula, find the 3x3
grid with the highest total value. Uses a 1D partial sum.

### Advent of Code 2018, Day 11, Part 2

Link: https://adventofcode.com/2018/day/11

Given a 300x300 grid that's filled in based on a formula, find the NxN
square with the highest total value. Uses a 1D partial sum, which isn't
super fast, and this could be improved by going to a 2D partial sum.

### Advent of Code 2018, Day 12, Part 1

Link: https://adventofcode.com/2018/day/12

Given a series of "pots" that may or may not contain a plant, apply growth/death
rules. Calculate a score after 20 cycles.

### Advent of Code 2018, Day 12, Part 2

Link: https://adventofcode.com/2018/day/12

Given a series of "pots" that may or may not contain a plant, apply growth/death
rules. Calculate a score after 50,000,000,000 cycles.

Trick is to detect the pattern in the cycles.

### Advent of Code 2018, Day 13, Part 1 and Part 2

Link: https://adventofcode.com/2018/day/13

Given carts on a track, simulate the carts traveling around the track and
predicting collisions.

### Advent of Code 2018, Day 14, Part 1

Link: https://adventofcode.com/2018/day/14

Given a cyclical recipe game, figure out the 10 scores after the number of
target cycles.

### Advent of Code 2018, Day 14, Part 2

Link: https://adventofcode.com/2018/day/14

Given a cyclical recipe game, figure out when a sequence of scores appears.

### Advent of Code 2018, Day 15, Part 1

Link: https://adventofcode.com/2018/day/15

Given a map of elves and goblins, simulate a battle according to some
very fiddly rules to get right.

### Advent of Code 2018, Day 15, Part 2

Link: https://adventofcode.com/2018/day/15

Given a map of elves and goblins, simulate a battle according to some
very fiddly rules to get right. In part2, we adjust the elves "power" until
they win without any losses.

### Advent of Code 2018, Day 16, Part 1

Link: https://adventofcode.com/2018/day/16

Given a list of "samples" for output from a CPU's registers, figure out what
operation codes are possible, and compute how many have more than three
possibilities.

### Advent of Code 2018, Day 16, Part 2

Link: https://adventofcode.com/2018/day/16

Given a list of "samples" for output from a CPU's registers, figure out what
operation codes correspond to what functions using process of elimination.
Afterward, run the "test program" and return first register value.

### Advent of Code 2018, Day 17, Part 1 and Part 2

Link: https://adventofcode.com/2018/day/17

Given a list of clay tile coordinates, simulate water flowing down, filling
various capture points and overflowing.

### Advent of Code 2018, Day 18, Part 1

Link: https://adventofcode.com/2018/day/18

Given a lumber map of empty spaces, trees, and lumberyards, simulate how
the acreage changes in make-up. Calculate score after 10 cycles.

### Advent of Code 2018, Day 18, Part 2

Link: https://adventofcode.com/2018/day/18

Given a lumber map of empty spaces, trees, and lumberyards, simulate how
the acreage changes in make-up. For Part 2, simulate 1000000000 cycles

### Advent of Code 2018, Day 19, Part 1

Link: https://adventofcode.com/2018/day/19

Given a program that runs on the CPU from day 16, run the program and
display what's on "register 0".

### Advent of Code 2018, Day 19, Part 2

Link: https://adventofcode.com/2018/day/19

Given a program that runs on the CPU from day 16, run the program and
display what's on "register 0" when setting register 0 to 1.

This is impractically slow to run, so the puzzle required disassembling
what it actually did, which turned out to be the sum of the factors of a
number that it calculates internally.

### Advent of Code 2018, Day 20, Part 1 and Part 2

Link: https://adventofcode.com/2018/day/20

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

### Advent of Code 2018, Day 21, Part 1

Link: https://adventofcode.com/2018/day/21

Given a program that runs on the CPU from day 16, figure out what number
will cause the program to exit. Just intercepts the test where it does the
exit and re-injects that number.

### Advent of Code 2018, Day 21, Part 1

Link: https://adventofcode.com/2018/day/21

Given a program that runs on the CPU from day 16, figure out what number
will cause the program to execute "the most number of instructions". The
algorithm produces a repeating stream of numbers, so it has to figure out
what the last number it produces before it repeats.

The algorithm itself is very slow to execute on the pseudo-CPU, so it required
analyzing the algorithm. The semi-optimized version that still does things
more-or-less the same way takes 55 seconds. I also boiled down the algorithm
into optimized Python that does it in 4ms.

The algorithm itself is a hashing function that feeds the same number in over
and over, which eventually causes a repeating cycle.

I would imagine the puzzle varies the two constants, which are read from the
program data for these optimized versions.

### Advent of Code 2018, Day 22, Part 1

Link: https://adventofcode.com/2018/day/22

Given an algorithm that determines a map of caves with certain
attributes, calculate the total of the attributes for a given region.

### Advent of Code 2018, Day 22, Part 2

Link: https://adventofcode.com/2018/day/22

Given an algorithm that determines a map of caves with certain attributes, and
rules about how the cave system can be followed, calculate the shortest path.

### Advent of Code 2018, Day 23, Part 1 and Part 2

Link: https://adventofcode.com/2018/day/23

Given a set of "bot" coordinates and a scanning manhattan-distance radius, figure out:
Part 1: How many bots in range of the bot with the largest radius.
Part 2: What position is in range of the most bots and closest to 0,0,0 origin.

Part 2 is tricky and requires dividing a bounding cuboid into smaller and smaller
regions, and keeping a priority queue to hone in on the best coordinate.

### Advent of Code 2018, Day 24, Part 1 and Part 2

Link: https://adventofcode.com/2018/day/24

Given a battle between an "infection" and an "immune system" that follows certain
rules, simulate the battle.
Part 1: Determine the outcome based on the input data.
Part 2: Calculate minimum boost to immune system to get a winning outcome.

### Advent of Code 2018, Day 25

Link: https://adventofcode.com/2018/day/25

Given a list of four-dimensional stars, calculate number of "constellations"
where the stars are within 3 units of each other (manhattan distance)

