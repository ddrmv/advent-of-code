from typing import Dict

def hash_str(input):
    current_value = 0
    for char in input.rstrip():
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value

def process_input(input):
    return (instruction_string for instruction_string in input.rstrip().split(','))

def dash_operation(box: dict, label):
    box.pop(label, None)

def eq_operation(box: dict, label, focal_length):
    box[label] = focal_length

def focusing_power(boxes: dict[int, dict[str, int]]):
    total = 0
    for boxes_key in boxes:
        for box_index, lens_label in enumerate(boxes[boxes_key]):
            total += (boxes_key + 1) * (box_index + 1) * boxes[boxes_key][lens_label]
    return total

def print_boxes(boxes):
    for box_key in boxes:
        if boxes[box_key]:
            print(box_key, boxes[box_key])


def part1(input):
    return sum(hash_str(s) for s in process_input(input))

def part2(input):
    boxes: dict[int, dict[str, int]]
    boxes = dict()
    for i in range(256):
        boxes[i] = dict()

    for instruction_string in process_input(input):
        if '-' in instruction_string:
            label = instruction_string[:-1]
            box_hash = hash_str(label)
            dash_operation(boxes[box_hash], label)
        else:
            label, focal_length = instruction_string.split('=')
            box_hash = hash_str(label)
            eq_operation(boxes[box_hash], label, int(focal_length))

    return focusing_power(boxes)