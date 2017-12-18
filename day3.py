#!/usr/bin/env python

import math

import click


@click.command()
@click.argument('input_file', type=click.Path(exists=True))
def cli(input_file):
    the_input = parse_input(input_file)

    print(part1(the_input))
    print(part2(the_input))


def parse_input(input_file):
    return int(open(input_file, 'r').read().strip())


def part1(the_input):
    return main(the_input)


def part2(the_input):
    exit(0)
    return main(the_input)


def main(the_input):
    left = (-1, 0)
    right = (1, 0)
    down = (0, -1)
    up = (0, 1)

    num = the_input

    odd_num = get_odd_num(num)

    top_right, top_left, bottom_left, bottom_right = get_corners(odd_num)

    steps_to_square = []

    steps_to_square += [right] * max((bottom_right - max(num, bottom_left)), 0)
    steps_to_square += [down] * max((bottom_left - max(num, top_left)), 0)
    steps_to_square += [left] * max((top_left - max(num, top_right)), 0)
    steps_to_square += [up] * max((top_right - num), 0)

    steps_from_square = steps_from_odd_square(odd_num)

    steps_to_one = steps_to_square + steps_from_square

    total_steps_to_one = [0, 0]
    for x, y in steps_to_one:
        total_steps_to_one[0] += x
        total_steps_to_one[1] += y

    total_steps = sum(abs(steps) for steps in total_steps_to_one)

    return total_steps


def steps_from_odd_square(odd_num):
    left = (-1, 0)
    up = (0, 1)

    if odd_num == 1:
        return []
    else:
        return [left, up] + steps_from_odd_square(odd_num - 2)


# return smallest odd integer such that the square of that integer is greater
# than or equal to the given number
def get_odd_num(num):
    the_num = math.ceil(math.sqrt(num))
    is_even = the_num % 2 == 0

    if is_even:
        the_num += 1

    return the_num


# list of numbers
# top_right, top_left, bottom_left, bottom_right
def get_corners(num):
    top_left = (num ** 2) - (2*num) + 2
    top_right = (num ** 2) - (3*num) + 3
    bottom_left = (num ** 2) - num + 1
    bottom_right = num ** 2

    return [top_right, top_left, bottom_left, bottom_right]



if __name__ == '__main__':
    cli()
