from part1_d3 import item_value

def find_badge(backpacks):
    return set(backpacks[0]).intersection(set(backpacks[1])).intersection(set(backpacks[2])).pop()

def total_badges(input):
    backpacks = input.rstrip().split('\n')
    groups = []
    for i in range(0, len(backpacks)-2, 3):
        groups.append(backpacks[i:i+3])
    return sum(item_value(find_badge(group)) for group in groups)