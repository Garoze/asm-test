#!/usr/bin/env python3

# Reference:
# https://github.com/garyexplains/examples/blob/master/vASM.py

import re
from sys import argv

from table import Opcode_t
from opcodes import Instructions, Modes, Address

def write_out(b):
    with open("out.bin", "ab") as out:
        out.write(bytearray(b))

def get_mode(value: str) -> Modes:
    """
    Return the right mode from a value
    example: LDI #FFFF -> IMM mode I16
    """
    match value:
        case "#": return Modes.IMM
        case "$": return Modes.ABS
        case   _: return Modes.IMP

def LSB(value: str) -> int:
    """
    Return the LSB of a value
    example: ABCD -> CD
    """
    return int(f'0x{value[1:]}', 16) & 0x00FF

def MSB(value):
    """
    Return the MSB of a value
    example: ABCD -> AB
    """
    return (int(f'0x{value[1:]}', 16) & 0xFF00) >> 8

def make_instruction(instruction: tuple, value: str = ""):
    """
    Generate the byte for a instruction
    """
    match instruction[1]:
        case Modes.IMP:
            return [instruction[0]]
        case Modes.IMM:
            match instruction[2]:
                case Address.IM8:
                    return [instruction[0], LSB(value)]
                case Address.I16:
                    return [instruction[0], LSB(value), MSB(value)]
        case Modes.ABS:
            return [instruction[0], LSB(value), MSB(value)]

def main():
    with open('out.bin', "wb") as out:
        out.close()

    with open(argv[1]) as f:
        for line in f:
            if line[0] in ';.':
                continue

            line  = line.replace('\n', '').replace('\r', '')
            token = re.split(r'[, ]', line)

            instruction = Opcode_t[token[0].upper()]

            match instruction[1]:
                case Modes.IMP:
                    b = make_instruction(instruction)
                    print(b)
                case Modes.IMM:
                    value = token[1]
                    b = make_instruction(instruction, value)
                    print(b)
                case Modes.ABS:
                    value = token[1]
                    b = make_instruction(instruction, value)
                    print(b)

if __name__ == '__main__':
    if len(argv) < 2:
        print(f"usage: {argv[0]} <file_path>")
        exit(1)
    else:
        main()
