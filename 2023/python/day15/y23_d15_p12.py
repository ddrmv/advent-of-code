from typing import List

def hash_str(input):
    current_value = 0
    for char in input.rstrip():
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value

def process_input(input):
    return (instruction_string for instruction_string in input.rstrip().split(','))


def part1(input):
    return sum(hash_str(s) for s in process_input(input))
