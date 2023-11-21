import string

def item_value(item):
    if item in string.ascii_lowercase:
        return string.ascii_lowercase.find(item) + 1
    else:
        return string.ascii_uppercase.find(item) + 27

def backpack_score(backpack):
    half = len(backpack)//2
    repeating_item = set(backpack[0:half]).intersection(set(backpack[half:]))
    return item_value(repeating_item.pop())

def total_score(input_string):
    return sum(backpack_score(line) for line in input_string.rstrip().split('\n'))