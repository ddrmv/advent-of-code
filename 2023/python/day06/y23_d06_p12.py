from functools import reduce
from typing import List
from bisect import bisect_left


class Race():
    def __init__(self, time, record):
        self.time = time
        self.record = record

    def __str__(self):
        return f"{self.time}-{self.record};"

    def move_distance(self, speed):
        move_time = self.time - speed
        return speed * move_time

    def is_win(self, speed):
        return self.move_distance(speed) > self.record

    def ways_to_win(self):
        ways = 0
        for speed in range(1, self.time):
            if self.is_win(speed):
                ways += 1
        return ways
    
    def find_a_win_logn(self, min, max):
        if self.is_win((max - min) // 2):
            return (max - min) // 2
        return self.find_a_win_logn(min, max//2) or self.find_a_win_logn(max//2, max)

    def ways_to_win_bisect(self):
        found_win = self.find_a_win_logn(1, self.time)
        speeds_upto_found_win = list(range(1, found_win + 1))
        min_win_speed = bisect_left(speeds_upto_found_win, 1, key=lambda speed: self.is_win(speed))
        speeds_after_found_win = list(range(self.time, found_win, -1))
        position = bisect_left(speeds_after_found_win, 1, key=lambda speed: self.is_win(speed))
        max_win_speed = speeds_after_found_win[position]
        return max_win_speed - min_win_speed


def nums_str_to_nums_list(st):
    return [int(num) for num in st.split(' ') if num.isdigit()]

def nums_str_to_concat_num(st):
    return int("".join(st.split(':')[1].replace(' ', '')))

def process_input(input):
    races = []
    times_part, distances_part = input.rstrip().split('\n')
    times = nums_str_to_nums_list(times_part.split(':')[1])
    distances = nums_str_to_nums_list(distances_part.split(':')[1])
    for time, distance in zip(times, distances):
        races.append(Race(time, distance))
    return races

def process_input_p2(input):
    times_part, distances_part = input.rstrip().split('\n')
    time = nums_str_to_concat_num(times_part)
    distance = nums_str_to_concat_num(distances_part)
    return Race(time, distance)


def part1(input):
    races: List[Race]
    races = process_input(input)
    ways_list = [race.ways_to_win() for race in races]
    return reduce(lambda a,b: a*b, ways_list)

def part2(input):
    race: Race
    race = process_input_p2(input)
    return race.ways_to_win_bisect()
