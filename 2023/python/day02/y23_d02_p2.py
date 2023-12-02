from functools import reduce

def update_cubes_required_for_play(play, required):
    for cubes_of_color in play.split(", "):
        number, color = cubes_of_color.split(" ")
        if required[color] < int(number):
            required[color] = int(number)

def cubes_required_for_game(game):
    required = {"green": 0, "red": 0, "blue": 0}
    plays_part = game.split(": ")[1]
    for play in plays_part.split("; "):
        update_cubes_required_for_play(play, required)
    return required

def part2(input):
    total = 0
    for game in input.rstrip().split("\n"):
        cubes = cubes_required_for_game(game)
        calculate_power = lambda a, b: a*b
        total += reduce(calculate_power, cubes.values())
    return total