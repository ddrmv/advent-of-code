from typing import Dict, List
from itertools import chain

class Direction():
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __str__(self):
        return f'd:{self.row},{self.col}'

    def __eq__(self, other) -> bool:
        if not isinstance(other, Direction):
            return False
        return self.row == other.row and self.col == other.col
    
    def __hash__(self) -> int:
        return hash((self.row, self.col))


DIR = {'u': Direction(-1, 0), 'd': Direction(+1, 0),
       'l': Direction(0, -1), 'r': Direction(0, +1)}


class Tile():
    def __init__(self, char: str):
        self.type: str
        self.empty: bool
        self.split: str
        self.beams_directions: list
        self.energized: int
        self.type = char
        self.empty = True if self.type == '.' else False
        self.lean = '/' if self.type == '/' else '\\' if self.type == '\\' else None
        self.split = '|' if self.type == '|' else '-' if self.type == '-' else None
        self.beams_directions = []
        self.energized = None

    def __str__(self) -> str:
        return self.type


class Beam():
    def __init__(self, row, col, d: Direction) -> None:
        self.row = row
        self.col = col
        self.d = d

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Beam):
            return False
        return (self.row == other.row
                and self.col == other.col
                and self.d == other.d)

    def __hash__(self):
        return hash((self.row, self.col, self.d.__hash__()))
    
    def __str__(self):
        return f'[{self.row}x{self.col}>{str(self.d)}#{self.__hash__()}]'

    def next_tile_coords(self) -> (int, int):
        return (self.row + self.d.row, self.col + self.d.col)
    
    def update(self, row, col, d: Direction):
        self.row = row
        self.col = col
        self.d = d

class Grid():
    def __init__(self):
        self.tiles: list[list[Tile]]
        self.beams: set
        self.tiles = []
        self.beams = set()
        self.rows = None
        self.cols = None


    def __str__(self):
        return '\n'.join((''.join((str(tile) for tile in line)) for line in self.tiles))
        
    def build_grid(self, input: str):
        for line_index, line in enumerate(input.split('\n')):
            self.tiles.append([])
            for char in line:
                self.tiles[line_index].append(Tile(char))
        self.rows = len(self.tiles)
        self.cols = len(self.tiles[0])

    def add_beam(self, beam: Beam):
        self.beams.add(beam)

    def is_in_grid(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols

    def beam_tick(self):
        new_dir_after_lean: dict[tuple(str, Direction), Direction]
        new_dir_after_lean = {('/', DIR['d']): DIR['l'],
                              ('/', DIR['u']): DIR['r'],
                              ('/', DIR['l']): DIR['d'],
                              ('/', DIR['r']): DIR['u'],
                              ('\\', DIR['d']): DIR['r'],
                              ('\\', DIR['u']): DIR['l'],
                              ('\\', DIR['l']): DIR['u'],
                              ('\\', DIR['r']): DIR['d']}
        perpendiculars: dict[Direction, tuple(Direction, Direction)]
        perpendiculars = {DIR['u']: (DIR['l'], DIR['r']),
                          DIR['d']: (DIR['l'], DIR['r']),
                          DIR['l']: (DIR['u'], DIR['d']),
                          DIR['r']: (DIR['u'], DIR['d'])}

        beam: Beam
        self.tiles: list[list[Tile]]

        while self.beams:
            beam = self.beams.pop()
            next_row, next_col = beam.next_tile_coords()

            if not self.is_in_grid(next_row, next_col):
                # beam is discarded
                continue

            next_tile: Tile
            next_tile = self.tiles[next_row][next_col]
            if beam.d in next_tile.beams_directions:
                # beam is discarded
                continue

            next_tile.energized = True
            next_tile.beams_directions.append(beam.d)

            if next_tile.empty:
                beam.update(next_row, next_col, beam.d)
                self.beams.add(beam)
                continue

            if next_tile.lean != None:
                new_dir = new_dir_after_lean[(next_tile.lean, beam.d)]
                beam.update(next_row, next_col, new_dir)
                self.beams.add(beam)
                continue

            if next_tile.split == '|':
                if beam.d == DIR['u'] or beam.d == DIR['d']:
                    beam.update(next_row, next_col, beam.d)
                    self.beams.add(beam)
                elif beam.d == DIR['l'] or beam.d == DIR['r']:
                    new_dir_1, new_dir_2 = perpendiculars[beam.d]
                    beam.update(next_row, next_col, new_dir_1)
                    self.beams.add(beam)
                    new_beam = Beam(next_row, next_col, new_dir_2)
                    self.beams.add(new_beam)
                continue

            if next_tile.split == '-':
                if beam.d == DIR['l'] or beam.d == DIR['r']:
                    beam.update(next_row, next_col, beam.d)
                    self.beams.add(beam)
                elif beam.d == DIR['u'] or beam.d == DIR['d']:
                    new_dir_1, new_dir_2 = perpendiculars[beam.d]
                    beam.update(next_row, next_col, new_dir_1)
                    self.beams.add(beam)
                    new_beam = Beam(next_row, next_col, new_dir_2)
                    self.beams.add(new_beam)
                continue

            assert False, 'invalid next_tile type + beam direction combination'

    def print_energized(self):
        output = ''
        for line in self.tiles:
            for tile in line:
                output += '#' if tile.energized else '.'
            output += '\n'
        return output

    def count_energized(self):
        total = 0
        for row in self.tiles:
            for tile in row:
                if tile.energized:
                    total += 1
        return total


def part1(input: str):
    g = Grid()
    g.build_grid(input.rstrip())
    g.add_beam(Beam(0,-1,DIR['r']))
    g.beam_tick()
    return g.count_energized()

def part2(input: str):
    input = input.rstrip()
    g = Grid()
    g.build_grid(input)

    top_range =    (Beam(-1, col, DIR['d']) for col in range(g.cols))
    bottom_range = (Beam(g.rows, col, DIR['u']) for col in range(g.cols))
    left_range =   (Beam(row, -1, DIR['r']) for row in range(g.rows))
    right_range =  (Beam(row, g.cols, DIR['l']) for row in range(g.rows))

    max_energized = 0
    for beam in chain(top_range, bottom_range, left_range, right_range):
        g = Grid()
        g.build_grid(input)
        g.add_beam(beam)
        g.beam_tick()
        current_energized = g.count_energized()
        if max_energized < current_energized:
            max_energized = current_energized

    return max_energized