def process_input(input: str):
    return [int(n) for n in input.strip().split()]

cache = dict()

def blink(n, times):
    if times == 1:
        if n == 0:
            return 1
        if len(str(n)) % 2 == 0:
            return 2
        else:
            return 1
    else:
        if (n, times) in cache:
            return cache[(n, times)]
        else:
            if n == 0:
                cache[(n, times)] = blink(1, times - 1)
                return cache[(n, times)]
            len_n = len(str(n))
            if len_n % 2 == 0:
                half_digits = 10 ** (len_n//2)
                n2 = n % half_digits
                n1 = n // half_digits
                cache[(n, times)] = blink(n1, times - 1) + blink(n2, times - 1)
                return cache[(n, times)]
            else:
                cache[(n, times)] = blink(n * 2024, times - 1)
                return cache[(n, times)]

def part1(input):
    stones = process_input(input)
    blinks = 25
    return sum([blink(n, blinks) for n in stones])


def part2(input):
    stones = process_input(input)
    blinks = 75
    return sum([blink(n, blinks) for n in stones])
