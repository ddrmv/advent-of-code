import pytest
import os
from part1and2 import find_biggest_backpack, find_top_three_backpacks

@pytest.fixture
def example_input():
  return '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
'''

@pytest.fixture
def full_input():
  dirname = os.path.dirname(__file__)
  filename = os.path.join(dirname, '../../input/day01')
  with open(filename) as file:
    full_input = file.read()
    return full_input

def test_find_most_calories(full_input, example_input):
  assert find_biggest_backpack(example_input) == 24000
  assert find_biggest_backpack(full_input) == 75622

def test_find_top_three_backpacks(full_input):
  assert find_top_three_backpacks(full_input) == 213159