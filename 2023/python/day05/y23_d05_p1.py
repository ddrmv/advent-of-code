from typing import List
from functools import reduce

class MapRange():
    def __init__(self, dest_start, source_start, range_length):
        self.dest_start = dest_start
        self.source_start = source_start
        self.range_length = range_length

    def __str__(self):
        return f"{self.dest_start},{self.source_start},{self.range_length};"

    def is_in_range(self, num):
        return self.source_start <= num < self.source_start + self.range_length
    
    def output_for(self, num):
        '''Gives mapped destination for provided source'''
        assert self.is_in_range(num) # to remove
        return self.dest_start + (num - self.source_start)


class GardenMap():
    def __init__(self, name, map_ranges):
        self.name = name
        self.map_ranges = [MapRange(*mr) for mr in map_ranges]

    def output_for(self, num):
        '''Gives mapped destination for provided source'''
        for mr in self.map_ranges:
            if mr.is_in_range(num):
                return mr.output_for(num)
        return num
    
    def __str__(self):
        output = f"m:{self.name} "
        for mr in self.map_ranges:
            output += str(mr)
        return output

def nums_str_to_nums_list(st):
    return [int(num) for num in st.split(' ')]

def parse_seeds_part1(string):
    return nums_str_to_nums_list(string)

def parse_input(input, seed_parser):
    seeds_part = input[:input.find('\n\n')]
    seeds = seed_parser(seeds_part.split(': ')[1])
    map_strings = input.rstrip().split('\n\n')[1:]
    maps = []
    for map_string in map_strings:
        map_name = map_string[:map_string.find(' map')]
        map_ranges_strings = map_string.split('\n')[1:]
        map_ranges = [tuple(nums_str_to_nums_list(mrs)) for mrs in map_ranges_strings]
        maps.append(GardenMap(map_name, map_ranges))
    return seeds, maps

def seed_to_location(seed: int, maps: List[GardenMap]):
    next_step = seed
    for m in maps:
        next_step = m.output_for(next_step)
    return next_step

def part1(input):
    seeds, maps = parse_input(input, parse_seeds_part1)
    locations = [seed_to_location(seed, maps) for seed in seeds]
    return min(locations)
