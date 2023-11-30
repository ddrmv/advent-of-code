import pytest
import os
from part1_d8 import part1, is_visible_row

@pytest.fixture
def example_input():
    return '''30373
25512
65332
33549
35390'''

@pytest.fixture
def full_input():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../../input/day08')
    with open(filename) as file:
        full_input = file.read()
        return full_input

def test_is_visible_row():
    assert is_visible_row([[3,3,3],[3,3,3],[3,3,3]], 1, 1) == False
    assert is_visible_row([[2,3,3],[3,3,3],[3,3,3]], 1, 1) == False
    assert is_visible_row([[3,3,3],[3,3,2],[3,3,3]], 1, 1) == True
    assert is_visible_row([[3,3,3],[2,3,3],[3,3,3]], 1, 1) == True

def test_part1(example_input, full_input):
    assert part1(example_input) == 21
    assert part1(full_input) == 1676