from math import inf
from bisect import bisect_right
from itertools import chain
from typing import List


class MapRange():
    def __init__(self, dest_start, source_start, range_length):
        self.dest_start = dest_start
        self.source_start = source_start
        self.range_length = range_length

    def __lt__(self, other):
        return self.source_start < other.source_start

    def __str__(self):
        return f"{self.dest_start},{self.source_start},{self.range_length};"

    def is_in_range(self, num):
        return self.source_start <= num < self.source_start + self.range_length
    
    def output_for(self, num):
        '''Gives mapped destination for provided source'''
        return self.dest_start + (num - self.source_start)


class GardenMap():
    def __init__(self, name, map_ranges: List[MapRange]):
        self.name = name
        self.map_ranges = [MapRange(*mr) for mr in map_ranges]
        self.number_of_ranges = len(map_ranges)

    def __str__(self):
        output = f"m:{self.name} "
        for mr in self.map_ranges:
            output += str(mr)
        return output

    def output_for(self, num):
        '''Gives mapped destination for provided source'''
        correct_map_range = bisect_right(self.map_ranges, num, key=lambda mr: mr.source_start)
        if correct_map_range == 0:
            return num
        elif correct_map_range == self.number_of_ranges:
            if not self.map_ranges[correct_map_range - 1].is_in_range(num):
                return num
        return self.map_ranges[correct_map_range - 1].output_for(num)
    
    def sort_by_source(self):
        self.map_ranges.sort()


def nums_str_to_nums_list(st):
    return [int(num) for num in st.split(' ')]

def parse_seeds_part1(string):
    return nums_str_to_nums_list(string)

def parse_seeds_part2(string):
    nums = [int(num) for num in string.split(' ')]
    seeds_ranges = []
    for index in range(0, len(nums), 2):
        seeds_ranges.append(range(nums[index], nums[index] + nums[index+1]))
    return chain.from_iterable(seeds_ranges)

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

def seed_to_location(seed: int, garden_maps: List[GardenMap]):
    next_step = seed
    for gm in garden_maps:
        next_step = gm.output_for(next_step)
    return next_step


def part1(input):
    seeds, garden_maps = parse_input(input, parse_seeds_part1)
    for gm in garden_maps:
        gm.sort_by_source()
    locations = [seed_to_location(seed, garden_maps) for seed in seeds]
    return min(locations)

def part2(input):
    garden_maps: List[GardenMap]
    seeds, garden_maps = parse_input(input, parse_seeds_part2)

    for gm in garden_maps:
        gm.sort_by_source()

    min_location = inf
    for seed in seeds:
        location = seed_to_location(seed, garden_maps)
        if location < min_location:
            min_location = location
    return min_location