#!/usr/bin/env python

import click

@click.command()
@click.argument('input_string', type=str)
def main(input_string):
    digits = [int(num) for num in list(input_string)]

    digits.append(digits[0])

    the_sum = 0

    for i in range(len(digits) - 1):
        if digits[i] == digits[i+1]:
            the_sum += digits[i]

    print(the_sum)


if __name__ == '__main__':
    main()
