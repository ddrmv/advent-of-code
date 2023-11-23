def is_full_overlap(pair):
    elves = pair.split(",")
    first_elf = [int(n) for n in elves[0].split('-')]
    second_elf = [int(n) for n in elves[1].split('-')]
    return (second_elf[0] >= first_elf[0] and second_elf[1] <= first_elf[1] or
        second_elf[0] <= first_elf[0] and second_elf[1] >= first_elf[1])

def full_overlaps(input):
    full_overlaps = 0
    for line in input.strip().split('\n'):
        if is_full_overlap(line):
            full_overlaps += 1
    return full_overlaps
    