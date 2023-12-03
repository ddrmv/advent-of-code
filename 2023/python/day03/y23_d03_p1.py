import re
from functools import reduce


class Node():
    def __init__(self, x, y):
        self.x = x           # line
        self.y = y           # index

    def __str__(self):
        return f"x:{self.x},y:{self.y}"

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def get_node_toward(self, row_change, col_change):
        return Node(self.x + row_change, self.y + col_change)


class EngineNumber():
    def __init__(self, number, line_num, number_start_index):
        self.number = int(number)
        self.row = line_num
        self.lindex = number_start_index
        self.rindex = number_start_index + len(number) - 1

    def __str__(self):
        return f"N:{self.number}, {self.row}/{self.lindex}/{self.rindex}"
    
    def __hash__(self):
        return hash((self.number, self.row, self.lindex, self.rindex))

    def __eq__(self, o):
        return self.line_num == o.line_num and self.rindex == o.lindex and self.lindex == o.rindex


class Engine():
    def __init__(self, input):
        self.engine_lines = input.rstrip().split("\n")
        self.engine_map = [[char for char in row] for row in self.engine_lines]
        self.symbols = None
        self.engine_rows = None
        self.engine_cols = None
        self.engine_numbers = []
        self.stars = []
        self.parse_input()

    def __str__(self):
        return f"{self.engine_rows}x{self.engine_cols}"

    def parse_input(self):
        self.find_engine_rows_cols()
        self.find_symbol_set()
        self.find_engine_numbers()

    def find_engine_rows_cols(self):
        self.engine_cols = len(self.engine_lines[0])
        self.engine_rows = len(self.engine_lines)

    def find_symbol_set(self):
        self.symbols = set("".join(self.engine_lines))
        not_symbols = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '\n', '.'}
        self.symbols.difference_update(not_symbols)

    def find_engine_numbers(self):
        for line_num, line in enumerate(self.engine_lines):
            numbers_in_line = re.findall(r'\d+', line)
            search_from = 0
            for number in numbers_in_line:
                number_start_index = line.find(number, search_from)
                self.engine_numbers.append(EngineNumber(number, line_num, number_start_index))
                search_from = number_start_index + len(number)

    def is_digit(self, node, row=0, col=0):
        node_to_check = node.get_node_toward(row, col)
        return self.engine_map[node_to_check.x][node_to_check.y].isdigit()

    def get_engine_number_by_node(self, node):
        chars_left = 0
        while node.y - chars_left - 1 >= 0 and self.is_digit(Node(node.x, node.y - chars_left - 1)):
            chars_left += 1
        chars_right = 0
        while node.y + chars_right + 1 < self.engine_cols and self.is_digit(Node(node.x, node.y + chars_right + 1)):
            chars_right += 1
        number_string = self.engine_lines[node.x][node.y - chars_left : node.y + chars_right + 1]
        return number_string

    def gear_ratio(self, star: Node):
        assert self.engine_map[star.x][star.y] == '*'
        close_nodes = []
        offsets = {(-1, -1), (-1, 0),  (-1, 1), (0, -1), (0, 1),  (1, -1), (1, 0),  (1, 1)}
        for offset in offsets:
            if 0 <= star.x + offset[0] < self.engine_rows:
                if 0 <= star.y + offset[1] < self.engine_cols:
                    close_nodes.append(Node(star.x + offset[0], star.y + offset[1]))
        close_nodes_with_digits = [x for x in close_nodes if self.is_digit(x)]

        close_engine_numbers = set()
        for node in close_nodes_with_digits:
            close_engine_numbers.add(self.get_engine_number_by_node(node))

        if len(close_engine_numbers) == 2:
            return reduce(lambda a,b: int(a) * int(b), close_engine_numbers)
        return 0

    def get_adjacent_set(self, e_n: EngineNumber):
        top, left, right, bottom = None, None, None, None

        top = max(0, e_n.row - 1)
        bottom = min(self.engine_rows, e_n.row + 1)
        left = max(0, e_n.lindex - 1)
        right = min(self.engine_cols, e_n.rindex + 1)

        adjacents = ""
        for line in self.engine_lines[top:bottom + 1]:
            adjacents += line[left:right + 1]

        return set(adjacents)
    
    def is_part(self, e_n: EngineNumber):
        return len(self.get_adjacent_set(e_n).intersection(self.symbols)) > 0

    def find_gear_ratio_total(self):
        gear_ratios = []
        for line_num, line in enumerate(self.engine_lines):
            search_from = 0
            while True:
                found_index = line.find('*', search_from)
                if found_index < 0:
                    break
                gear_ratios.append(self.gear_ratio(Node(line_num, found_index)))
                search_from = found_index + 1
        return sum(gear_ratios)


def part1(input):
    engine = Engine(input)
    return sum(e_n.number for e_n in filter(engine.is_part, engine.engine_numbers))


def part2(input):
    engine = Engine(input)
    return engine.find_gear_ratio_total()