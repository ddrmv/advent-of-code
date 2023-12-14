import pytest
from mylib.helper import read_input
from y23_d14_p1 import part1

@pytest.fixture
def example_input():
    return read_input('y23_14_e.txt')

@pytest.fixture
def full_input():
    return read_input('y23_14.txt')

def test_part1(example_input):
    assert part1(example_input) == 136

def test_part1_full(full_input):
    assert part1(full_input) == 113424