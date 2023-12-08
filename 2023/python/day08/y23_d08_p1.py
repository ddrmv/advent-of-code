from typing import List, Dict

def process_input(input):
    pattern, directions_part = input.split('\n\n')
    nodes = dict()
    for line in directions_part.split('\n'):
        node, left, right = line[:3], line[7:10], line[12:15]
        nodes[node] = (left, right)
    direction_to_index = {'L': 0, 'R': 1}
    route = [direction_to_index[direction] for direction in pattern]
    return route, nodes

def part1(input):
    route: List[int]
    nodes: Dict()
    route, nodes = process_input(input)
    
    current_node = nodes['AAA']
    steps = 0
    while True:
        for step_direction in route:
            next_step = current_node[step_direction]
            if next_step == 'ZZZ':
                return steps + 1
            current_node = nodes[next_step]
            steps += 1
