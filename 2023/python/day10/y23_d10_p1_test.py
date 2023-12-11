import pytest
from mylib.helper import read_input
from y23_d10_p1 import part1

@pytest.fixture
def example_input():
    return read_input('y23_10_e.txt')

@pytest.fixture
def example_input_2():
    return read_input('y23_10_e2.txt')

@pytest.fixture
def full_input():
    return read_input('y23_10.txt')

def test_part1(example_input, example_input_2, full_input):
    assert part1(example_input) == 4
    assert part1(example_input_2) == 8
    assert part1(full_input) == 7107
