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
            write_out([instruction[0]])
            return 1
        case Modes.IMM:
            match instruction[2]:
                case Address.IM8:
                    write_out([instruction[0], LSB(value)])
                    return 2
                case Address.I16:
                    write_out([instruction[0], LSB(value), MSB(value)])
                    return 3
        case Modes.ABS:
            write_out([instruction[0], LSB(value), MSB(value)])
            return 3
    return 0

def valid_opcode(opcode: str) -> bool:
    return opcode in Opcode_t

def parse_labels():
    pass

def as_hex(value):
    return "0x{:04X}".format(value)

LABELS_TABLE = {}

def main():
    PC = 0x0000

    with open('out.bin', "wb") as out:
        out.close()

    with open(argv[1]) as f:
        for n, line in enumerate(f):
            if line[0] in '.':
                label = line[1:].split(':')[0]
                if not label in LABELS_TABLE:
                    LABELS_TABLE[label] = PC
                else:
                    print(f"Line: {n} Label -> {label} already defined with the value: {as_hex(LABELS_TABLE[label])}")

            line  = line.replace('\n', '').replace('\r', '').lstrip()
            token = re.split(r'[, ]', line)

            opcode = token[0].upper()

            if (valid_opcode(opcode)):
                match len(token):
                    case 1:
                        instruction = get_instruction(opcode, Modes.IMP)
                        PC += make_instruction(instruction)
                    case 2:
                        if token[1] in LABELS_TABLE:
                            value = "$" + str(LABELS_TABLE[token[1]])
                            instruction = get_instruction(opcode, Modes.ABS)
                            PC += make_instruction(instruction, value)
                        else:
                            value = token[1]
                            mode  = get_mode(value)
                            instruction = get_instruction(opcode, mode)
                            PC += make_instruction(instruction, value)

if __name__ == '__main__':
    if len(argv) < 2:
        print(f"usage: {argv[0]} <file_path>")
        exit(1)
    else:
        main()

