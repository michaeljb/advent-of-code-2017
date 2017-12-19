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


def part2(the_input):
    LEFT = (0, -1)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    UP = (-1, 0)

    the_grid = [[0 for x in range(11)] for y in range(11)]

    the_grid[5][5] = 1

    def next_index(x, y):
        print('\nx, y = ', (x,y))

        offset = -5

        # set origin to 0,0
        x = x + offset
        y = y + offset

        # layer 0, 1, 2, etc?
        N = max(abs(coord) for coord in (x, y))

        on_bottom = x == N
        on_right = y == N
        on_top = x == -N
        on_left = y == -N

        # print('N:', N)
        # print('x,y', (x,y))

        # print('on_bottom', on_bottom)
        # print('on_right', on_right)
        # print('on_top', on_top)
        # print('on_left', on_left)

        # order of these ifs *matters*
        if on_bottom:
            direction = RIGHT

        elif on_left:
            direction = DOWN

        elif on_top:
            direction = LEFT

        elif on_right:
            direction = UP

        the_next = (x + direction[0], y + direction[1])

        the_next = (the_next[0] - offset, the_next[1] - offset)

        print('the_next = ', the_next)

        return the_next

    def surrounding_indices(x, y):
        return [
            (x - 1, y - 1),
            (x - 1, y),
            (x - 1, y + 1),
            (x, y + 1),
            (x + 1, y + 1),
            (x + 1, y),
            (x + 1, y - 1),
            (x, y - 1)
        ]

    def surrounding_sum(x, y):
        return sum(the_grid[x][y] for x, y in surrounding_indices(x, y))

    current_index = (5, 5)
    new_value = 0
    while new_value <= the_input:
        current_index = next_index(*current_index)
        new_value = surrounding_sum(*current_index)
        x, y = current_index
        the_grid[x][y] = new_value

    from pprint import pprint
    pprint(the_grid)

    return new_value


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
    top_right = (num ** 2) - (3*num) + 3
    top_left = (num ** 2) - (2*num) + 2
    bottom_left = (num ** 2) - num + 1
    bottom_right = num ** 2

    return [top_right, top_left, bottom_left, bottom_right]



if __name__ == '__main__':
    cli()
