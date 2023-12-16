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
        self.beams_directions: list[Direction]
        self.energized: int
        self.type = char
        self.empty = True if self.type == '.' else False
        self.lean = '/' if self.type == '/' else '\\' if self.type == '\\' else None
        self.split = '|' if self.type == '|' else '-' if self.type == '-' else None
        self.beams_directions = []
        self.energized = 0

    def __str__(self) -> str:
        return self.type

    def is_energized(self):
        return self.energized > 0


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
        return hash((self.row, self.col, self.d.row, self.d.col))
    
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
        self.tiles[beam.row][beam.col].energized += 1

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

        cycles = 0
        while len(self.beams) > 0 and cycles < 1000:
            cycles += 1
            beams_to_remove = set()
            beams_to_add = set()
            beam: Beam
            for beam in self.beams:
                next_row, next_col = beam.next_tile_coords()
                if not self.is_in_grid(next_row, next_col):
                    beams_to_remove.add(beam)
                else:
                    next_tile: Tile
                    next_tile = self.tiles[next_row][next_col]
                    next_tile.energized += 1
                    if next_tile.empty:
                        beam.update(next_row, next_col, beam.d)
                    elif next_tile.lean != None:
                        new_dir = new_dir_after_lean[(next_tile.lean, beam.d)]
                        beam.update(next_row, next_col, new_dir)
                    elif next_tile.split != None:
                        if (next_tile.split == '|' and (beam.d == DIR['u'] or beam.d == DIR['d'])):
                            beam.update(next_row, next_col, beam.d)
                        elif (next_tile.split == '-' and (beam.d == DIR['l'] or beam.d == DIR['r'])):
                            beam.update(next_row, next_col, beam.d)
                        elif ((next_tile.split == '|' and (beam.d == DIR['l'] or beam.d == DIR['r']))
                           or (next_tile.split == '-' and (beam.d == DIR['u'] or beam.d == DIR['d']))):
                            new_dir_1, new_dir_2 = perpendiculars[beam.d]
                            beam.update(next_row, next_col, new_dir_1)
                            beam_to_add = Beam(next_row, next_col, new_dir_2)
                            if beam_to_add not in self.beams:
                                beams_to_add.add(beam_to_add)
                        else:
                            assert False, 'invalid combnation of split and direction'
                    else:
                        assert False, 'next_tile should be empty, lean or split'

            self.beams = self.beams.union(beams_to_add)

            self.beams = self.beams - beams_to_remove

            self.beams = set(list(self.beams))


    def print_energized(self):
        output = ''
        for line in self.tiles:
            for tile in line:
                output += '#' if tile.energized > 0 else '.'
            output += '\n'
        return output

    def count_energized(self):
        total = 0
        for row in self.tiles:
            for tile in row:
                if tile.energized > 0:
                    total += 1
        return total


def part1(input: str):
    g = Grid()
    g.build_grid(input.rstrip())
    g.add_beam(Beam(0,0,DIR['r']))
    g.beam_tick()
    return g.count_energized()
