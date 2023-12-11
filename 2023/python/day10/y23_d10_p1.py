from typing import List
# PIPE_TYPE = {'.': (None, None), '|': ((-1,0), (1, 0))}


class Node():
    def __init__(self, row, col, type: str = '.'):
        self.row = row
        self.col = col
        self.type = type
        self.con1 = None
        self.con2 = None
        self.set_connections()

    def set_connections(self):
        match self.type:
            case '.':
                self.con1, self.con2 = None, None
            case '|':
                self.con1, self.con2 = (-1, 0), (1, 0)
            case '-':
                self.con1, self.con2 = (0, -1), (0, 1)
            case 'L':
                self.con1, self.con2 = (-1, 0), (0, 1)
            case 'J':
                self.con1, self.con2 = (-1, 0), (0, -1)
            case '7':
                self.con1, self.con2 = (1, 0), (0, -1)
            case 'F':
                self.con1, self.con2 = (1, 0), (0, 1)
            case 'S':
                self.con1, self.con2 = None, None
            case _:
                raise ValueError
            
    def set_start_connections(self, con1, con2):
        self.con1 = con1
        self.con2 = con2
            
    def __eq__(self, other):
        return self.row == other.row and self.col == other.col and self.type == other.type

    def __str__(self):
        return f'{self.type}'
    

class Grid():
    def __init__(self):
        self.nodes: List[Node]
        self.start: Node
        self.nodes = []
        self.start = None
        self.rows = None
        self.cols = None

    def __str__(self):
        output = ''
        for row in self.nodes:
            for col in row:
                output += str(col)
            output += '\n'
        return output

    def build_grid(self, input):
        rows = input.split('\n')
        for row_i, row in enumerate(rows):
            self.nodes.append([Node(row_i, col_i, char) for col_i, char in enumerate(row)])
        self.rows = len(self.nodes)
        self.cols = len(self.nodes[0])
        self.start = self.identify_start()

    def get_node_neighbor(self, node: Node, offsets):
        row_offset, col_offset = offsets[0], offsets[1]
        return self.nodes[node.row + row_offset][node.col + col_offset]

    def find_start_connections(self):
        cons = []
        for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_node: Node
            next_node = self.get_node_neighbor(self.start, direction)
            if next_node.type != '.':
                next_node_con1 = self.get_node_neighbor(next_node, next_node.con1)
                next_node_con2 = self.get_node_neighbor(next_node, next_node.con2)
                if self.start == next_node_con1 or self.start == next_node_con2:
                    cons.append(direction)
        return cons
    
    def identify_start(self):
        for row in self.nodes:
            for node in row:
                if node.type == 'S':
                    return node
                
    def update_start(self):
        start_connections = self.find_start_connections()
        self.start.set_start_connections(*start_connections)

    def next_pipe_in_ring(self, current_node: Node, previous_node: Node):
        con1 = self.get_node_neighbor(current_node, current_node.con1)
        con2 = self.get_node_neighbor(current_node, current_node.con2)
        return con1 if con1 != previous_node else con2
    
    def find_main_loop_length(self):
        next_pipe = self.get_node_neighbor(self.start, self.start.con1)
        previous_pipe = self.start
        loop_len = 1
        while next_pipe != self.start:
            previous_pipe, next_pipe = next_pipe, self.next_pipe_in_ring(next_pipe, previous_pipe)
            loop_len += 1
        return loop_len

def part1(input):
    grid = Grid()
    grid.build_grid(input.rstrip())
    grid.update_start()
    out = grid.find_main_loop_length()
    return out//2