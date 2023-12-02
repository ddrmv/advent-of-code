import os, pytest
from y23_d02_p2 import part2

@pytest.fixture
def example_input():
    return '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''

@pytest.fixture
def full_input():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../../input/day02')
    with open(filename) as file:
        full_input = file.read()
        return full_input
    
def test_part2(example_input, full_input):
    assert part2(example_input) == 2286
    assert part2(full_input) == 65371