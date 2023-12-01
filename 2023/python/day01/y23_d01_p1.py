import string

def get_first_num(line):
    for char in line:
        if char in string.digits:
            return char

def get_last_num(line):
    for char in reversed(line):
        if char in string.digits:
            return char

def part1(input):
    numbers = []
    for line in input.rstrip().split("\n"):
        first_num = get_first_num(line)
        last_num = get_last_num(line)
        numbers.append(int(first_num + last_num))
    return sum(numbers)