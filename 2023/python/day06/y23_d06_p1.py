from functools import reduce
from typing import List


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


def nums_str_to_nums_list(st):
    return [int(num) for num in st.split(' ') if num.isdigit()]

def process_input(input):
    races = []
    times_part, distances_part = input.rstrip().split('\n')
    times = nums_str_to_nums_list(times_part.split(':')[1])
    distances = nums_str_to_nums_list(distances_part.split(':')[1])
    for time, distance in zip(times, distances):
        races.append(Race(time, distance))
    return races


def part1(input):
    races = List[Race]
    races = process_input(input)

    ways_list = [race.ways_to_win() for race in races]
    return reduce(lambda a,b: a*b, ways_list)