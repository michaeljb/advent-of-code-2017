#!/usr/bin/env python

import click


@click.command()
@click.argument('part', type=int, default=1)
@click.argument('input_file', type=click.Path(exists=True))
def main(part, input_file):
    return {
        1: part1
    }[part](input_file)


def part1(input_file):
    input_string = open(input_file, 'r').read().strip()
    digits = [int(num) for num in list(input_string)]

    digits.append(digits[0])

    the_sum = 0

    for i in range(len(digits) - 1):
        if digits[i] == digits[i+1]:
            the_sum += digits[i]

    print(the_sum)


if __name__ == '__main__':
    main()
