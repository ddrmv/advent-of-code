from typing import List

class Pattern():
    def __init__(self, input):
        self.lines = [line for line in input.split('\n')]
        self.grid = [[char for char in line] for line in self.lines]
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])

    def find_horizontal_mirror_line(self):
        for row in range(0, self.rows - 1):
            if self.lines[row] == self.lines[row + 1]:
                mir_before = row
                mir_after = row + 1
                still_mirror = True
                while mir_before - 1 >= 0 and mir_after + 1 < self.rows:
                    mir_before -= 1
                    mir_after += 1
                    if self.lines[mir_before] != self.lines[mir_after]:
                        still_mirror = False
                        break
                if still_mirror:
                    return row
        return None

    def find_vertical_mirrors_per_line(self, line):
        potential_mirrors = set()
        first_line = line
        for col in range(0, self.cols - 1):
            if first_line[col] == first_line[col + 1]:
                mir_before = col
                mir_after = col + 1
                still_mirror = True
                while mir_before - 1 >= 0 and mir_after + 1 < self.cols:
                    mir_before -= 1
                    mir_after += 1
                    if first_line[mir_before] != first_line[mir_after]:
                        still_mirror = False
                        break
                if still_mirror:
                    potential_mirrors.add(col)
        return potential_mirrors
    
    def find_vertical_mirror_line(self):
        first_line = self.lines[0]
        potential_mirrors = self.find_vertical_mirrors_per_line(first_line)
        for line in self.lines[1:]:
            potential_mirrors_in_line = self.find_vertical_mirrors_per_line(line)
            potential_mirrors.intersection_update(potential_mirrors_in_line)
            if len(potential_mirrors) == 0:
                return None
        assert len(potential_mirrors) == 1
        return potential_mirrors.pop()


def part1(input):
    total = 0
    pattern: Pattern
    for pattern_part in input.rstrip().split('\n\n'):
        pattern = Pattern(pattern_part)

        horizontal_mirror_line = pattern.find_horizontal_mirror_line()
        if horizontal_mirror_line != None:
            total += (horizontal_mirror_line + 1) * 100

        vertical_mirror_line = pattern.find_vertical_mirror_line()
        if vertical_mirror_line != None:
            total += vertical_mirror_line + 1

    return total