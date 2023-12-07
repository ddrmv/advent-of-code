import pytest
from mylib.helper import read_input
from y23_d05_p1 import MapRange, GardenMap, part1, part2

@pytest.fixture
def example_input():
    return read_input('y23_05_e.txt')

@pytest.fixture
def full_input():
    return read_input('y23_05.txt')

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

def test_part2_example(example_input):
    assert part2(example_input) == 46

@pytest.mark.skip(reason="naive solution, slow")
def test_part2_full_input(full_input):
    assert part2(full_input) == 2254686