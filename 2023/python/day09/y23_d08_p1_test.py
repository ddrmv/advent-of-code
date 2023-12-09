import pytest
from mylib.helper import read_input
from y23_d08_p1 import part1, part2

@pytest.fixture
def example_input():
    return read_input('y23_09_e.txt')

@pytest.fixture
def full_input():
    return read_input('y23_09.txt')

def test_part1(example_input, full_input):
    assert part1(example_input) == 114
    assert part1(full_input) == 114

def test_part1(example_input, full_input):
    assert part2(example_input) == 2
    assert part2(full_input) == 1154