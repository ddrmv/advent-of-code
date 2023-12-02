import os, pytest
from y23_d02_p1 import play_is_possible, game_is_possible, part1

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

@pytest.fixture
def bag1():
    return {"green": 13, "red": 12, "blue": 14}

def test_play_is_possible(bag1):
    assert play_is_possible("3 blue, 4 red", bag1) == True
    assert play_is_possible("1 red, 2 green, 6 blue", bag1) == True
    assert play_is_possible("2 green", bag1) == True
    assert play_is_possible("20 green", bag1) == False

def test_game_is_possible(bag1):
    assert game_is_possible(
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", bag1) == (True, 1)
    assert game_is_possible(
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        bag1) == (False, 3)

def test_part1(example_input, full_input, bag1):
    assert part1(example_input, bag1) == 8
    assert part1(full_input, bag1) == 3059