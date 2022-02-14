#!/usr/bin/env python3

# Reference:
# https://github.com/garyexplains/examples/blob/master/vASM.py

import re
import codecs
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
        case Modes.LBE:
            return Opcode_t[instruction]["L"]

def get_mode(value: str = "") -> Modes:
    """
    Return the right mode from a value
    example: LDI #FFFF -> IMM mode I16
    """
    v = value[0]
    match v:
        case "#": return Modes.IMM
        case "$": return Modes.ABS
        case "L": return Modes.LBE
        case   _: return Modes.IMP

def LSB(value: str) -> int:
    """
    Return the LSB of a value
    example: ABCD -> CD
    """
    LSB = (int(value[1:], 16) & 0x00FF)
    return LSB

def MSB(value):
    """
    Return the MSB of a value
    example: ABCD -> AB
    """
    MSB = (int(value[1:], 16) & 0xFF00) >> 8
    return MSB

def as_hex(value):
    return "0x{:04X}".format(value)

def make_instruction(instruction: tuple, value: str = ""):
    """
    Generate the byte for a instruction
    """
    match instruction[1]:
        case Modes.IMP:
            write_buffer([instruction[0]])
            return 1
        case Modes.IMM:
            match instruction[2]:
                case Address.IM8:
                    write_buffer([instruction[0], LSB(value)])
                    return 2
                case Address.I16:
                    write_buffer([instruction[0], LSB(value), MSB(value)])
                    return 3
        case Modes.ABS:
            write_buffer([instruction[0], LSB(value), MSB(value)])
            return 3
        case Modes.LBE:
            write_buffer([instruction[0], value])
            return 3

    return 0

def valid_opcode(opcode: str) -> bool:
    return opcode in Opcode_t


BUFFER = []
LABELS_TABLE = {}

def write_out(b):
    buffer = resolve_labels(b)
    with open("out.bin", "ab") as out:
        for instruction in buffer:
            out.write(bytearray(instruction))

def write_buffer(b):
    BUFFER.append(b)

def parse_labels():
    with open(argv[1]) as f:
        for n, line in enumerate(f):
            if line[0] in '.':
                line  = line.replace('\n', '').replace('\r', '').lstrip()
                label = line[1:].split(':')[0]
                if not label in LABELS_TABLE:
                    LABELS_TABLE[label] = 0
                else:
                    print(f"{argv[1][2:]}:{n} Error: symbol `{label}` is already defined -> {as_hex(LABELS_TABLE[label])}")

def resolve_labels(b):
    buffer = []
    for instruction in b:
        if len(instruction) > 1:
            if type(instruction[1]) == str:
                label = instruction[1][1:]
                if label in LABELS_TABLE:
                    value = str(LABELS_TABLE[label])
                    buffer.append([instruction[0], LSB(f'L{value}'), MSB(f'L{value}')])
                pass
            else:
                buffer.append(instruction)
        else:
            buffer.append(instruction)

    return buffer

def inc_pc(pc, n):
    """
    Increment the PC by n amount
    and keep the Hex format
    """
    inc = int(pc, 16) + n
    return hex(inc)

def main():
    PC = hex(0)

    with open('out.bin', "wb") as out:
        out.close()

    parse_labels()

    with open(argv[1]) as f:
        for n, line in enumerate(f):
            if line[0] in '.':
                line  = line.replace('\n', '').replace('\r', '').lstrip()
                label = line[1:].split(':')[0]
                LABELS_TABLE[label] = PC
            else:
                line  = line.replace('\n', '').replace('\r', '').lstrip()
                token = re.split(r'[, ]', line)

                opcode = token[0].upper()

                if (valid_opcode(opcode)):
                    match len(token):
                        case 1:
                            instruction = get_instruction(opcode, Modes.IMP)
                            n = make_instruction(instruction)
                            PC = inc_pc(PC, n)
                        case 2:
                            if token[1][0] in '#$':
                                value = token[1]
                                mode = get_mode(value)
                                instruction = get_instruction(opcode, mode)
                                n = make_instruction(instruction, value)
                                PC = inc_pc(PC, n)
                            else:
                                value = f'L{token[1]}'
                                mode = get_mode(value)
                                instruction = get_instruction(opcode, mode)
                                n = make_instruction(instruction, value)
                                PC = inc_pc(PC, n)
                        case _:
                            print(f"Something went wrong PC: {PC}")
                else:
                    print(f"Invalid Opcode: {opcode}")

        write_out(BUFFER)


if __name__ == '__main__':
    if len(argv) < 2:
        print(f"usage: {argv[0]} <file_path>")
        exit(1)
    else:
        main()

