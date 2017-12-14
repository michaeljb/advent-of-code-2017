#!/usr/bin/env python

import re

import click


@click.command()
@click.argument('input_file', type=click.Path(exists=True))
def main(input_file):
    txt = open(input_file, 'r').read()

    lines = txt.split('\n')

    checksum = 0

    for line in lines:
        if len(line) == 0:
            continue
        numbers = [int(num) for num in re.split('\s+', line)]

        checksum += max(numbers) - min(numbers)

    print(checksum)



if __name__ == '__main__':
    main()
