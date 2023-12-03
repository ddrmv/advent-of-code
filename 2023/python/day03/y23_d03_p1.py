import re

class EngineNumber():
    def __init__(self, number, line_num, number_start_index):
        self.number = int(number)
        self.row = line_num
        self.lindex = number_start_index
        self.rindex = number_start_index + len(number) - 1

    def __str__(self):
        return f"N:{self.number}, {self.row}/{self.lindex}/{self.rindex}"


class Engine():
    def __init__(self, input):
        self.engine_lines = input.rstrip().split("\n")
        self.symbols = None
        self.engine_rows = None
        self.engine_cols = None
        self.engine_numbers = []
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


def part1(input):
    engine = Engine(input)
    return sum(e_n.number for e_n in filter(engine.is_part, engine.engine_numbers))