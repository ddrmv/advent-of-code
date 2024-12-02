def get_lists(input):
    left = []
    right = []

    # read left and right list
    for line in input[:-1].split('\n'):
        left_value, right_value = line.strip().split("   ")
        left.append(int(left_value))
        right.append(int(right_value))
    
    left.sort()
    right.sort()

    return left, right


def part1(input):
    left, right = get_lists(input)

    # get difference
    difference = 0
    for left_value, right_value in zip(left, right):
        difference += abs(left_value - right_value)

    return difference


def part2(input):
    left, right = get_lists(input)
    
    left_hash = dict()
    right_hash = dict()

    # count nums in right
    for num in right:
        if num in right_hash:
            right_hash[num] += 1
        else:
            right_hash[num] = 1

    # count nums in left
    for num in left:
        if num in left_hash:
            left_hash[num] += 1
        else:
            left_hash[num] = 1

        if num not in right_hash:
            right_hash[num] = 0

    similarity_score = 0
    for num in left_hash:
        similarity_score += num * left_hash[num] * right_hash[num]
    
    return similarity_score

