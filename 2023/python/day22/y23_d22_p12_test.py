import pytest
from mylib.helper import read_input
from y23_d22_p12 import part1, part2

@pytest.fixture
def example_input():
    return read_input('y23_22_e.txt')

@pytest.fixture
def full_input():
    return read_input('y23_22.txt')

def test_part1(example_input):
    assert part1(example_input) == 5

def test_part1_full(full_input):
    assert part1(full_input) == 527

def test_part2(example_input):
    assert part2(example_input) == 7

def test_part2_full(full_input):
    assert part2(full_input) == 100376