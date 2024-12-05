import pytest
from mylib.helper import read_input
from y24_d04_p12 import part1, part2

@pytest.fixture
def example_input():
    return read_input('y24_04_e.txt')

@pytest.fixture
def example_input_2():
    return read_input('y24_04_e2.txt')

@pytest.fixture
def example_input_3():
    return read_input('y24_04_e3.txt')

@pytest.fixture
def full_input():
    return read_input('y24_04.txt')

def test_part1(example_input):
    assert part1(example_input) == 18

def test_part1_smaller(example_input_2):
    assert part1(example_input_2) == 4

def test_part1_full(full_input):
    assert part1(full_input) == 2718

def test_part2_smaller(example_input_3):
    assert part2(example_input_3) == 1

def test_part2_small(example_input):
    assert part2(example_input) == 9

def test_part2_full(full_input):
    assert part2(full_input) == 2046
