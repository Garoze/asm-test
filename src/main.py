#!/usr/bin/env python3

# Reference:
# https://github.com/garyexplains/examples/blob/master/vASM.py

import re
from sys import argv

from table import Opcode_t
from opcodes import Instructions, Modes, Address

def get_instruction(instruction: str, mode: Modes = Modes.IMP):
    match mode:
        case Modes.IMM:
            return Opcode_t[instruction]["#"]
        case Modes.ABS:
            return Opcode_t[instruction]["$"]
        case Modes.IMP:
            return Opcode_t[instruction]["_"]

def get_mode(value: str = "") -> Modes:
    """
    Return the right mode from a value
    example: LDI #FFFF -> IMM mode I16
    """
    v = value[0]
    match v:
        case "#": return Modes.IMM
        case "$": return Modes.ABS
        case   _: return Modes.IMP

def write_out(b):
    with open("out.bin", "ab") as out:
        out.write(bytearray(b))

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

def valid_opcode(opcode: str) -> bool:
    return opcode in Opcode_t

def main():
    with open('out.bin', "wb") as out:
        out.close()

    with open(argv[1]) as f:
        for line in f:
            if line[0] in ';.':
                continue

            line  = line.replace('\n', '').replace('\r', '')
            token = re.split(r'[, ]', line)

            opcode = token[0].upper()

            if (valid_opcode(opcode)):
                match len(token):
                    case 1:
                        instruction = get_instruction(opcode, Modes.IMP)
                        b = make_instruction(instruction)
                        write_out(b)
                    case 2:
                        value = token[1]
                        mode  = get_mode(value)
                        instruction = get_instruction(opcode, mode)
                        b = make_instruction(instruction, value)
                        write_out(b)

if __name__ == '__main__':
    if len(argv) < 2:
        print(f"usage: {argv[0]} <file_path>")
        exit(1)
    else:
        main()

