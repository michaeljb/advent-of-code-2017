#!/usr/bin/env python

import click


@click.command()
@click.argument('input_file', type=click.Path(exists=True))
def cli(input_file):
    the_input = parse_input(input_file)

    print(part1(the_input))
    print(part2(the_input))


def parse_input(input_file):
    return [int(num) for num in open(input_file, 'r').read().strip().split('\n')]


def part1(instructions):
    def instr_string(instr, addr, steps):
        instruction_strings = [str(i) for i in instr]

        try:
            instruction_strings[addr] = '(' + instruction_strings[addr] + ')'
        except IndexError:
            pass

        return str(steps) + ': ' + ' '.join(instruction_strings)

    address = 0
    instruction = 0
    steps = 0

    while address in range(len(instructions)):
        # print(instr_string(instructions, address, steps))
        instruction = instructions[address]

        instructions[address] += 1

        address = address + instruction

        steps += 1

    # print(instr_string(instructions, address, steps))

    return steps


def part2(the_input):
    exit(0)  # don't show part 2 output until part 2 is implemented
    return


if __name__ == '__main__':
    cli()
