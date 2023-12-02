def play_is_possible(play, bag):
    for cubes_of_color in play.split(", "):
        number, color = cubes_of_color.split(" ")
        if bag[color] < int(number):
            return False
    return True

def game_is_possible(line, bag):
    game_number_part, plays_part = line.split(": ")
    game_number = int(game_number_part.split(" ")[1])
    possible = True
    for play in plays_part.split("; "):
        if not play_is_possible(play, bag):
            possible = False
            break
    return (possible, game_number)

def part1(input, bag):
    possible_games_sum = 0
    for line in input.rstrip().split("\n"):
        possible, game_number = game_is_possible(line, bag)
        if possible:
            possible_games_sum += game_number
    return possible_games_sum