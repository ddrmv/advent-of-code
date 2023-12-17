import pytest
from mylib.helper import read_input
from y23_d16_p12 import part1, part2

@pytest.fixture
def example_input():
    return read_input('y23_16_e.txt')

@pytest.fixture
def full_input():
    return read_input('y23_16.txt')

def test_part1(example_input):
    assert part1(example_input) == 46

def test_part1_full(full_input):
    assert part1(full_input) == 7498

def test_part2(example_input):
    assert part2(example_input) == 51

def test_part2_full(full_input):
    assert part2(full_input) == 7846