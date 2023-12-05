import os, pytest
from y23_d05_p1 import MapRange, GardenMap, part1, part2

@pytest.fixture
def example_input():
    return '''seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
'''

@pytest.fixture
def full_input():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../../input/day05.txt')
    with open(filename) as file:
        full_input = file.read()
        return full_input
    

@pytest.fixture
def test_mr():
    return MapRange(50, 98, 2)

@pytest.fixture
def test_gm():
    gm = GardenMap("seed-to-soil", [(50, 98, 2), (52, 50, 48)])
    gm.sort_by_source()
    return gm


def test_MapRange(test_mr):
    assert test_mr.is_in_range(97) == False
    assert test_mr.is_in_range(99) == True
    assert test_mr.output_for(99) == 51

def test_GardenMap(test_gm):
    assert test_gm.output_for(5) == 5
    assert test_gm.output_for(53) == 55
    assert test_gm.output_for(99) == 51
    assert test_gm.output_for(200) == 200


def test_part1(example_input, full_input):
    assert part1(example_input) == 35
    assert part1(full_input) == 199602917

def test_part2(example_input, full_input):
    assert part2(example_input) == 46
    # naive solution, slow
    assert part2(full_input) == 2254686