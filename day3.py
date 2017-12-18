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
    num = the_input

    odd_num = get_odd_num(num)

    return odd_num


# return smallest odd integer such that the square of that integer is greater
# than or equal to the given number
def get_odd_num(num):
    the_num = math.ceil(math.sqrt(num))
    is_even = the_num % 2 == 0

    if is_even:
        the_num += 1

    return the_num


if __name__ == '__main__':
    cli()
