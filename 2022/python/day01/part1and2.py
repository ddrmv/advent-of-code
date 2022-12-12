def backpack_amount(backpack_string):
  item_calories = [int(item) for item in backpack_string.split("\n")]
  return sum(item_calories)

def calculate_backpacks(input):
  backpacks = input.rstrip().split("\n\n")
  backpack_amounts = [backpack_amount(pack) for pack in backpacks]
  return backpack_amounts

def find_biggest_backpack(input):
  backpack_amounts = calculate_backpacks(input)
  return max(backpack_amounts)

def find_top_three_backpacks(input):
  backpack_amounts = calculate_backpacks(input)
  backpack_amounts.sort()
  return sum(backpack_amounts[-3:])