def get_input(input: str):
    rules_part, updates_part = input[:-1].split("\n\n")
    updates = [[int(num) for num in line.split(",")] for line in updates_part.split("\n")]
    
    # rules in format (number 'key' must be before any element of rules_after[key])
    rules_after = dict()
    for line in rules_part.split("\n"):
        left, right = [int(num) for num in line.split("|")]
        if left in rules_after:
            rules_after[left].append(right)
        else:
            rules_after[left] = [right]
        if right not in rules_after:
            rules_after[right] = []

    return rules_after, updates

def is_valid_update(rules_after, update):
    for right in range(1, len(update)):
        for left in range(right):
            if update[right] not in rules_after[update[left]]:
                return False
    return True


def fix_update(rules_after, update):
    fixed_update = [update[0]]
    # if number is before the last element of fixed, check one on left until no rule, then add it there
    for e in update[1:]:
        current_position = len(fixed_update)
        placed = False
        while current_position > 0:
            if fixed_update[current_position - 1] in rules_after[e]:
                current_position -= 1
            else:
                fixed_update.insert(current_position, e)
                placed = True
                break
        if not placed:
            fixed_update.insert(0, e)
    return fixed_update


def part1(input):
    rules_after, updates = get_input(input)
    sum_of_middle_elements = 0

    for update in updates:
        if is_valid_update(rules_after, update):
            sum_of_middle_elements += update[len(update)//2]

    return sum_of_middle_elements


def part2(input):
    rules_after, updates = get_input(input)
    sum_of_middle_elements = 0

    for update in updates:
        if not is_valid_update(rules_after, update):
            update = fix_update(rules_after, update)
            sum_of_middle_elements += update[len(update)//2]

    return sum_of_middle_elements
