from math import inf

words = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
             "six": "6", "seven": "7", "eight": "8", "nine": "9",
             "1": "1", "2": "2", "3": "3", "4": "4", "5": "5",
             "6": "6", "7": "7", "8": "8", "9": "9"}

def find_first(line):
    '''Find leftmost number written as word or digit, return as str digit'''
    current_first_num, current_first_num_index = None, inf
    for key in words.keys():
        location = line.find(key)
        if location > -1 and location < current_first_num_index:
            current_first_num = words[key]
            current_first_num_index = location
    return current_first_num

def find_last(line):
    '''Find rightmost number written as word or digit, return as str digit'''
    current_last_num, current_last_num_index = None, -1
    for key in words.keys():
        location = line.rfind(key)
        if location > -1 and location > current_last_num_index:
            current_last_num = words[key]
            current_last_num_index = location
    return current_last_num

def part2(input):
    numbers = []
    for line in input.rstrip().split("\n"):
        first_num = find_first(line)
        last_num = find_last(line)
        numbers.append(int(first_num + last_num))
    return sum(numbers)