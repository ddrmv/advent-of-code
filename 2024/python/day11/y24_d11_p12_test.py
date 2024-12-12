import pytest
from mylib.helper import read_input
from y24_d11_p12 import part1, part2

@pytest.fixture
def example_input():
    return read_input('y24_11_e.txt')

@pytest.fixture
def full_input():
    return read_input('y24_11.txt')

def test_part1(example_input):
    assert part1(example_input) == 55312

def test_part1_full(full_input):
    assert part1(full_input) == 186203

def test_part2_full(full_input):
    assert part2(full_input) == 221291560078593
