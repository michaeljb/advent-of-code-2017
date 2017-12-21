#!/usr/bin/env python

import click


@click.command()
@click.argument('input_file', type=click.Path(exists=True))
def cli(input_file):
    print(part1(parse_input(input_file)))
    print(part2(parse_input(input_file)))


def parse_input(input_file):
    return


def part1(the_input):
    return


def part2(the_input):
    return


if __name__ == '__main__':
    cli()
