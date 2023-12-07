import pytest
from mylib.helper import read_input
from y23_d04_p12 import process_input, hits_to_value, part1, part2

@pytest.fixture
def example_input():
    return read_input('y23_04_e.txt')

@pytest.fixture
def full_input():
    return read_input('y23_04.txt')

def test_hits_to_value():
    assert hits_to_value(0) == 0
    assert hits_to_value(1) == 1
    assert hits_to_value(2) == 2
    assert hits_to_value(3) == 4
    assert hits_to_value(4) == 8

def test_part1(example_input, full_input):
    assert part1(example_input) == 13
    assert part1(full_input) == 25004

def test_part2(example_input, full_input):
    assert part2(example_input) == 30
    assert part2(full_input) == 14427616