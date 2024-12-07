import itertools
from collections import Counter

op = [0,1,2]    # 0 = +, 1 = *, 2 = "||"

# find unique permutations of a list of non-unique numbers (operations)
def permute_unique(nums):
    result = []
    counts = Counter(nums)
    len_nums = len(nums)

    def backtrack(current_permutation):
        # complete recursion path
        if len(current_permutation) == len_nums:
            result.append(current_permutation[:])
            return
        
        # iterate over unique numbers still available
        for num in counts:
            if counts[num] > 0:
                current_permutation.append(num)
                counts[num] -= 1
                
                # recurse to build the rest of the permutation
                backtrack(current_permutation)
                
                # backtrack
                current_permutation.pop()
                counts[num] += 1

    backtrack([])
    return result

def process_input(input: str):
    eqs = []
    for line in input.strip().split('\n'):
        eq_num, calibrations = line.split(": ")
        eq_num = int(eq_num)
        calibrations = [int(num) for num in calibrations.split()]
        eqs.append([eq_num, calibrations])
    return eqs


def part1(input):
    eqs = process_input(input)
    total_calibration = 0
    # check variations
    for eq in eqs:
        # operators list length
        ops_len = len(eq[1]) - 1
        multis = 0
        ops = [op[0] for _ in range(ops_len)]
        # for each combination of 0 "+"" and n "*"" to n "+" and  0 "*"
        for multis in range(ops_len + 1):
            added_multis = 0
            while added_multis < multis:
                ops[added_multis] = op[1]
                added_multis += 1
            unique_permutations = permute_unique(ops)

            match_found = False
            for per in unique_permutations:
                eq_result = eq[1][0]
                for idx, operation in enumerate(per):
                    if operation == op[0]:
                        eq_result += eq[1][idx + 1]
                    elif operation == op[1]:
                        eq_result *= eq[1][idx + 1]
                if eq_result == eq[0]:
                    total_calibration += eq_result
                    match_found = True
                    break

            if match_found:
                break

    return total_calibration


def part2(input):
    eqs = process_input(input)
    total_calibration = 0
    
    # build permutations of opoperations sequences at all lenghts up to maximum one in dataset

    # set memo_ops container to correct length
    memo_ops = []
    max_ops_in_dataset = max([len(e[1]) for e in eqs]) - 1
    for i in range(max_ops_in_dataset + 1):
        memo_ops.append([])

    # populate memo_ops
    for ops_len in range(max_ops_in_dataset + 1):
        # skip on no operations
        if ops_len == 0:
            continue

        # find cimbinations of number of operations
        op_number_combinations = []
        for i in range(ops_len + 1):
            for j in range(ops_len + 1 - i):
                for k in range(ops_len + 1 - i - j):
                    if i + j + k == ops_len:
                        op_counts = (i, j, k)
                        op_number_combinations.append(op_counts)

        # for each operator number combination run through all permutations
        ops = [op[0] for _ in range(ops_len)]
        for i, j, k in op_number_combinations:
            for x in range(i):
                ops[x] = 0
            for x in range(i, i+j):
                ops[x] = 1
            for x in range(i+j, i+j+k):
                ops[x] = 2

            memo_ops[ops_len].extend(permute_unique(ops))

    # check variations for each equotation for correctness
    for eq in eqs:
        # operators list length
        op_num = len(eq[1]) - 1
        ops_permutations = memo_ops[op_num]

        for per in ops_permutations:
            eq_result = eq[1][0]
            for idx, operation in enumerate(per):
                if operation == 0:
                    eq_result += eq[1][idx + 1]
                elif operation == 1:
                    eq_result *= eq[1][idx + 1]
                elif operation == 2:
                    eq_result = int(str(eq_result) + str(eq[1][idx + 1]))

            if eq_result == eq[0]:
                total_calibration += eq_result
                break

    return total_calibration
