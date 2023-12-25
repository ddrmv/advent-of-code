# formulas from:
# https://www.raymaps.com/index.php/how-to-find-point-of-intersection-of-two-lines/

from itertools import combinations


class Hailstone():
    def __init__(self, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

    def __str__(self):
        return f'{self.x},{self.y},{self.z}v{self.vx},{self.vy},{self.vz}'


def process_input(input: str):
    hailstones = []
    for line in input.rstrip().split('\n'):
        l = line.split()
        hs_str = l[0][:-1], l[1][:-1], l[2], l[4][:-1], l[5][:-1], l[6]
        hailstones.append(Hailstone(*tuple(int(n) for n in hs_str)))
    return hailstones


def part1(input, xy_min, xy_max):
    hs = process_input(input)
    a: Hailstone
    b: Hailstone

    collisions_in_test_area = 0
    for a, b in combinations(hs, 2):
        slope1 = a.vy/a.vx
        slope2 = b.vy/b.vx

        if slope1 == slope2:
            continue

        y_intercept1 = a.y - slope1 * a.x
        y_intercept2 = b.y - slope2 * b.x

        x = -(y_intercept1 - y_intercept2) / (slope1 - slope2)
        y = y_intercept1 + slope1 * x

        t1 = (x - a.x) / a.vx
        t2 = (x - b.x) / b.vx

        if t1 <= 0 or t2 <= 0:
            continue

        if (xy_min <= x <= xy_max and xy_min <= y <= xy_max):
            collisions_in_test_area += 1

    return collisions_in_test_area