from typing import List

def line_to_nums(s):
    return [int(num) for num in s.split(' ')]

def process_input(input):
    lines = input.rstrip().split('\n')
    return [line_to_nums(line) for line in lines]

def get_prediction_delta(a: List[int]):
    b = [b - a for a, b in zip(a, a[1:])]
    if b.count(0) == len(b):
        return 0
    else:
        return b[-1] + get_prediction_delta(b)

def get_prediction_delta_part2(a: List[int]):
    b = [b - a for a, b in zip(a, a[1:])]
    if b.count(0) == len(b):
        return 0
    else:
        return b[0] - get_prediction_delta_part2(b)

def part1(input):
    arrays = process_input(input)
    for array in arrays:
        print(array)
    return sum(array[-1] + get_prediction_delta(array) for array in arrays)

def part2(input):
    arrays = process_input(input)
    return sum(array[0] - get_prediction_delta_part2(array) for array in arrays)