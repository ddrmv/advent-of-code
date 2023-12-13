import pytest
from mylib.helper import read_input
from y23_d13_p2 import part2

@pytest.fixture
def example_input():
    return read_input('y23_13_e.txt')

@pytest.fixture
def full_input():
    return read_input('y23_13.txt')

def test_part2(example_input):
    assert part2(example_input) == 400

def test_part2_full(full_input):
    assert part2(full_input) == 42695