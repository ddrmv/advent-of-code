import pytest
from mylib.helper import read_input
from y23_d19_p2 import part2

@pytest.fixture
def example_input():
    return read_input('y23_19_e.txt')

@pytest.fixture
def full_input():
    return read_input('y23_19.txt')

def test_part2(example_input):
    assert part2(example_input) == 167409079868000

def test_part2_full(full_input):
    assert part2(full_input) == 128163929109524