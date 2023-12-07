import pytest
from mylib.helper import read_input
from y23_d06_p12 import part1, part2

@pytest.fixture
def example_input():
    return read_input('y23_06_e.txt')

@pytest.fixture
def full_input():
    return read_input('y23_06.txt')


def test_part1(example_input, full_input):
    assert part1(example_input) == 288
    assert part1(full_input) == 588588

def test_part2(example_input, full_input):
    assert part2(example_input) == 71503
    assert part2(full_input) == 34655848
