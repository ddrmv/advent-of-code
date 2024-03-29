import pytest
from mylib.helper import read_input
from y23_d07_p1 import Hand, part1

@pytest.fixture
def example_input():
    return read_input('y23_07_e.txt')
    
@pytest.fixture
def full_input():
    return read_input('y23_07.txt')

def test_Hand():
    assert Hand("32T3K", 765) < Hand("KTJJT", 220)
    assert Hand("KTJJT", 220) < Hand("QQQJA", 483)

def test_part1(example_input, full_input):
    assert part1(example_input) == 6440
    assert part1(full_input) == 249483956
