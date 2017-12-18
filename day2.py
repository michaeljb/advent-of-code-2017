#!/usr/bin/env python

import re

import click


@click.command()
@click.argument('input_file', type=click.Path(exists=True))
def cli(input_file):
    the_input = parse_input(input_file)

    print(part1(the_input))
    print(part2(the_input))


def parse_input(input_file):
    txt = open(input_file, 'r').read().strip()

    lines = txt.split('\n')

    return [[int(num) for num in re.split('\s+', line)] for line in lines]


def part1(lines):
    def checksum_func(line):
        return max(line) - min(line)

    return sum_all_lines(lines, checksum_func)


def part2(lines):
    def checksum_func(line):
        numbers = sorted(line)
        numbers_reversed = numbers[::-1]

        for divisor in numbers:
            smallest_dividend = 2 * divisor
            for dividend in (n for n in numbers_reversed if n >= smallest_dividend):
                quotient = dividend / divisor
                if quotient == int(quotient):
                    return int(quotient)

        return 0

    return sum_all_lines(lines, checksum_func)


def sum_all_lines(lines, checksum_func):
    return sum(checksum_func(line) for line in lines)


if __name__ == '__main__':
    cli()
