import pytest
import os
from y23_d01_p1 import get_first_num, get_last_num, part1

@pytest.fixture
def example_input():
    return '''1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
'''

@pytest.fixture
def full_input():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../../input/day01')
    with open(filename) as file:
        full_input = file.read()
        return full_input
  
def test_get_first_num():
    assert get_first_num("1abc2") == "1"
    assert get_first_num("treb7uchet") == "7"

def test_get_last_num():
    assert get_last_num("1abc2") == "2"
    assert get_last_num("a1b2c3d4e5f") == "5"
    assert get_last_num("treb7uchet") == "7"

def test_part1(example_input, full_input):
    assert part1(example_input) == 142
    assert part1(full_input) == 56506