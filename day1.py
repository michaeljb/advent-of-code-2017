#!/usr/bin/env python

import click


@click.command()
@click.argument('input_file', type=click.Path(exists=True))
def cli(input_file):
    the_input = parse_input(input_file)

    print(part1(the_input))
    print(part2(the_input))


def parse_input(input_file):
    input_string = open(input_file, 'r').read().strip()
    return [int(num) for num in list(input_string)]


def part1(digits):
    def next_index_func(index):
        return (index + 1) % len(digits)

    return sum_when_next_matches(digits, next_index_func)


def part2(digits):
    def next_index_func(index):
        return (index + int(len(digits) / 2)) % len(digits)

    return sum_when_next_matches(digits, next_index_func)


def sum_when_next_matches(digits, next_index_func):
    the_sum = 0

    for index in range(len(digits)):
        next_index = next_index_func(index)

        if digits[index] == digits[next_index]:
            the_sum += digits[index]

    return the_sum


if __name__ == '__main__':
    cli()
