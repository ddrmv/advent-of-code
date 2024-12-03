import re

def part1(input):
    mul_lines = input.split("mul(")
    pattern = r'^\d{1,3},\d{1,3}\)'
    total = 0
    for line in mul_lines:
        match = re.match(pattern, line)
        if match:
            num1, num2 = [int(num) for num in match.group()[:-1].split(',')]
            total += num1 * num2
    return total


def part2(input):
    lines_after_dont = input.split("don't()")
    # list of useful part, put first element as string starts as 'enabled'
    useful_parts = [lines_after_dont[0]]
    pattern = r'do\(\)'
    for line in lines_after_dont[1:]:
        result = re.split(pattern, line, maxsplit=1)
        useful_parts.extend(result[1:])

    # lines that start with "mul("
    mul_lines = []
    for line in useful_parts:
        if line.startswith("mul("):
            mul_lines.extend(line.split("mul("))
        else:
            mul_lines.extend(line.split("mul(")[1:])

    # find correct operation strings, same as part 1
    pattern = r'^\d{1,3},\d{1,3}\)'
    total = 0
    for line in mul_lines:
        match = re.match(pattern, line)
        if match:
            num1, num2 = [int(num) for num in match.group()[:-1].split(',')]
            total += num1 * num2

    return total
