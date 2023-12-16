from typing import Dict, List


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
        start_tile = self.tiles[0][0]
        direction = DIR['r']
        if start_tile.lean == '\\' or start_tile.split == '|':
            direction = DIR['d']
        elif start_tile.lean == '/':
            direction = DIR['u']
        beam = Beam(0,0,direction)
        self.beams.add(beam)
        first_tile: Tile
        first_tile = self.tiles[beam.row][beam.col]
        first_tile.energized = True
        first_tile.beams_directions.append(beam.d)

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
                continue  # beam is discarded

            next_tile: Tile
            next_tile = self.tiles[next_row][next_col]
            if beam.d in next_tile.beams_directions:
                continue  # beam is discarded

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
    g.beam_tick()
    return g.count_energized()