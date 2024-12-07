import pytest
from mylib.helper import read_input
from y24_d07_p12 import part1, part2

@pytest.fixture
def example_input():
    return read_input('y24_07_e.txt')

@pytest.fixture
def full_input():
    return read_input('y24_07.txt')

def test_part1(example_input):
    assert part1(example_input) == 3749

# passes in about a second
# def test_part1_full(full_input):
#     assert part1(full_input) == 5837374519342

def test_part2(example_input):
    assert part2(example_input) == 11387

# passes in about 32 seconds
# def test_part2_full(full_input):
#     assert part2(full_input) == 492383931650959
