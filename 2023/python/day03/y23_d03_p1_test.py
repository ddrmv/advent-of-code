import pytest
from mylib.helper import read_input
from y23_d03_p1 import part1, part2

@pytest.fixture
def example_input():
    return read_input('y23_03_e.txt')

@pytest.fixture
def full_input():
    return read_input('y23_03.txt')

def test_part1(example_input, full_input):
    assert part1(example_input) == 4361
    assert part1(full_input) == 536202

def test_part2(example_input, full_input):
    assert part2(example_input) == 467835
    assert part2(full_input) == 78272573