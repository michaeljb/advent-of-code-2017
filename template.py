#!/usr/bin/env python

import click


@click.command()
@click.argument('input_file', type=click.Path(exists=True))
def cli(input_file):
    the_input = parse_input(input_file)

    print(part1(the_input))
    print(part2(the_input))


def parse_input(input_file):
    return


def part1(the_input):
    return


def part2(the_input):
    exit(0)  # don't show part 2 output until part 2 is implemented
    return


if __name__ == '__main__':
    cli()
