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


def main(the_input, valid_passphrase_func):
    return len([p for p in the_input if valid_passphrase_func(p)])


def part1(the_input):
    def is_passphrase_valid(passphrase):
        return words_all_unique(passphrase)

    return main(the_input, is_passphrase_valid)


def words_all_unique(passphrase):
    words = passphrase.split(' ')

    word_count = len(words)

    unique_word_count = len(set(words))

    return unique_word_count == word_count


def no_anagrams(passphrase):
    words = passphrase.split(' ')

    words_with_chars_sorted = [tuple(sorted(word)) for word in words]

    num_anagrams = len(words) - len(set(words_with_chars_sorted))

    return num_anagrams == 0



def part2(the_input):
    def is_passphrase_valid(passphrase):
        return words_all_unique(passphrase) and no_anagrams(passphrase)

    return main(the_input, is_passphrase_valid)


if __name__ == '__main__':
    cli()
