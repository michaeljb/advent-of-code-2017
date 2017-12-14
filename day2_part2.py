#!/usr/bin/env python

import re

import click

@click.command()
@click.argument('input_file', type=click.Path(exists=True))
def main(input_file):
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

    txt = open(input_file, 'r').read()

    lines = txt.split('\n')

    checksum = 0

    for line in lines[:-1]:
        checksum += checksum_for_line(line)

    print(int(checksum))

if __name__ == '__main__':
    main()
