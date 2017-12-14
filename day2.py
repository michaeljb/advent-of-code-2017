#!/usr/bin/env python

import re

import click


@click.command()
@click.argument('part', type=int)
@click.argument('input_file', type=click.Path(exists=True))
def main(part, input_file):
    return {
        1: part1,
        2: part2
    }[part](input_file)


def part1(input_file):
    txt = open(input_file, 'r').read().strip()

    lines = txt.split('\n')

    checksum = 0

    for line in lines:
        if len(line) == 0:
            continue
        numbers = [int(num) for num in re.split('\s+', line)]

        checksum += max(numbers) - min(numbers)

    print(checksum)


def part2(input_file):
    def checksum_for_line(line):
        numbers = [int(num) for num in re.split('\s+', line)]
        numbers = sorted(numbers)

        numbers_reversed = numbers[::-1]

        for divisor in numbers:
            smallest_dividend_candidate = 2 * divisor
            for dividend in numbers_reversed:
                if dividend < smallest_dividend_candidate:
                    continue
                quotient = dividend / divisor
                if quotient == int(quotient):
                    return quotient

    txt = open(input_file, 'r').read().strip()

    lines = txt.split('\n')

    checksum = 0

    for line in lines:
        checksum += checksum_for_line(line)

    print(int(checksum))

if __name__ == '__main__':
    main()
