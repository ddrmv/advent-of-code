import pytest
import os
from part1_d6 import find_marker

@pytest.fixture
def example_input():
    return '''zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'''

@pytest.fixture
def full_input():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../../input/day06')
    with open(filename) as file:
        full_input = file.read()
        return full_input

def test_find_marker(example_input, full_input):
    assert find_marker(example_input, 4) == 11
    assert find_marker(full_input, 4) == 1235
    assert find_marker(example_input, 14) == 26
    assert find_marker(full_input, 14) == 3051