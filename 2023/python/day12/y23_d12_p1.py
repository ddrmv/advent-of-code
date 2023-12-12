from typing import List

class Group():
    def __init__(self, type: str, length: int, length_variation=0):
        self.type = type
        self.len = length
        self.max_len = length + length_variation

    def __str__(self):
        return f'{self.type}{self.len}-{self.max_len}, '

def produce_options(options, option, groups: List[Group], iteration, movable, chars):
    if iteration < len(groups):
        cur_g: Group
        cur_g = groups[iteration]
        if cur_g.type == '#':
            option += cur_g.type * cur_g.len
            produce_options(options, option, groups, iteration + 1, movable, chars)
        elif cur_g.type == '.':
            for active_len in range(cur_g.len, cur_g.max_len + 1):
                movable_used = active_len - cur_g.len
                if movable - movable_used >= 0:
                    add =  active_len * '.'
                    produce_options(options, option + add, groups, iteration + 1, movable - movable_used, chars)
    elif iteration == len(groups) and len(option) == chars:
        options.append(option)

def is_option_valid(option, springs):
    assert len(option) == len(springs)
    for op_char, sp_char in zip(option, springs):
        if op_char != sp_char and sp_char != '?':
            return False
    return True

def process_line(line_str):
    springs, damaged_groups = line_str.split(' ')

    damaged: List[int]  # eg. [3,2,1]
    damaged = [int(num) for num in damaged_groups.split(',')]

    total_damaged = sum(damaged)  # eg. 6
    num_damaged_groups = len(damaged)  # eg. 3
    springs_len = len(springs)
    min_operational_groups = num_damaged_groups - 1
    allocatable_operational = springs_len - total_damaged - min_operational_groups
    groups: List[Group]
    groups = []

    # groups of operational ('.')
    groups.append(Group('.', 0, allocatable_operational))
    for index, group_len in enumerate(damaged):
        if index != 0:
            groups.append(Group('.', 1, allocatable_operational))
        groups.append(Group('#', group_len))
    groups.append(Group('.', 0, allocatable_operational))
    
    options: List[str]
    options = []
    produce_options(options, '', groups, 0, allocatable_operational, springs_len)
    counter = 0
    for option in options:
        if is_option_valid(option, springs):
            counter += 1
    return counter


def part1(input):
    lines =  input.rstrip().split('\n')
    return sum(process_line(line) for line in lines)