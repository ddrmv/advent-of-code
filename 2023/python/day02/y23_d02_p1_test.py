import pytest
from mylib.helper import read_input
from y23_d02_p1 import play_is_possible, game_is_possible, part1

@pytest.fixture
def example_input():
    return read_input('y23_02_e.txt')

@pytest.fixture
def full_input():
    return read_input('y23_02.txt')

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