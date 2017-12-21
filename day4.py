#!/usr/bin/env python

import click


@click.command()
@click.argument('input_file', type=click.Path(exists=True))
def cli(input_file):
    the_input = parse_input(input_file)

    print(part1(the_input))
    print(part2(the_input))


def parse_input(input_file):
    return open(input_file, 'r').read().strip().split('\n')


def part1(the_input):
    valid_passphrases = [p for p in the_input if is_passphrase_valid(p)]

    return len(valid_passphrases)


def is_passphrase_valid(passphrase):
    words = passphrase.split(' ')

    word_count = len(words)

    unique_word_count = len(set(words))

    return unique_word_count == word_count


def part2(the_input):
    exit(0)  # don't show part 2 output until part 2 is implemented
    return


if __name__ == '__main__':
    cli()
