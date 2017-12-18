#!/usr/bin/env python

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
    return main(the_input)


def main(the_input):
    return the_input


if __name__ == '__main__':
    cli()
