import pytest
from mylib.helper import read_input
from y23_d15_p12 import part1, part2

@pytest.fixture
def example_input():
    return read_input('y23_15_e.txt')

@pytest.fixture
def full_input():
    return read_input('y23_15.txt')

def test_part1(example_input):
    assert part1(example_input) == 1320

def test_part1_full(full_input):
    assert part1(full_input) == 507666

def test_part2(example_input):
    assert part2(example_input) == 145

def test_part2_full(full_input):
    assert part2(full_input) == 233537