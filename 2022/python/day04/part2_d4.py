def is_any_overlap(pair):
    elves = pair.split(",")
    first_elf = [int(n) for n in elves[0].split('-')]
    second_elf = [int(n) for n in elves[1].split('-')]
    return (second_elf[0] >= first_elf[0] and second_elf[0] <= first_elf[1] or
        second_elf[1] >= first_elf[0] and second_elf[1] <= first_elf[1] or
        second_elf[0] >= first_elf[0] and second_elf[1] <= first_elf[1] or
        second_elf[0] <= first_elf[0] and second_elf[1] >= first_elf[1])

def any_overlaps(input):
    any_overlaps = 0
    for line in input.strip().split('\n'):
        if is_any_overlap(line):
            any_overlaps += 1
    return any_overlaps