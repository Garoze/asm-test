#!/usr/bin/env python3

# Reference:
# https://github.com/garyexplains/examples/blob/master/vASM.py

import re
from os import path
from sys import argv
from enum import IntFlag, auto

class Instructions(IntFlag):
    NOP = 0x00
    LDI = 0x01
    LDA = 0x02
    #  LDS = auto()
    STA = 0x04
    #  STS = auto()
    ADD = 0x06
    ADA = 0x07
    #  ADS = auto()
    SUB = 0x09
    SUA = 0x0A
    #  SUS = auto()
    MUL = 0x0C
    MUA = 0x0D
    #  MUS = auto()
    DIV = 0x0F
    DIA = 0x10
    #  DIS = auto()
    MOD = 0x03
    MOA = 0x04
    #  MOS = auto()
    #  INC = auto()
    #  DEC = auto()
    #  SHL = auto()
    #  SHR = auto()
    #  AND = auto()
    #  BOR = auto()
    #  XOR = auto()
    #  NOT = auto()
    #  PSH = auto()
    #  POP = auto()
    #  CMP = auto()
    #  CMA = auto()
    #  CMS = auto()
    #  JMP = auto()
    #  JMZ = auto()
    #  JNZ = auto()
    #  CAL = auto()
    #  RET = auto()
    #  OUT = auto()
    HLT = 0x28

class Mode(IntFlag):
    IMP = auto()
    IMM = auto()
    ABS = auto()

def usage(program):
    print(f"usage: {program} <file_path>")
    exit(1)

def write_out(b):
    with open("out.bin", "ab") as out:
        out.write(bytearray(b))

def make_instruction(instruction, mode, value = 0x00):
    match mode:
        case Mode.IMP:
            b  = [instruction]
            return b
        case Mode.IMM:
            imm16 = int(f'0x{value[1:]}', 16)
            b = [instruction, (imm16 & 0x00FF), (imm16 & 0xFF00) >> 8]
            return b
        case Mode.ABS:
            add16 = int(f'0x{value[1:]}', 16)
            b = [instruction, (add16 & 0x00FF), (add16 & 0xFF00) >> 8]
            return b

def main():
    with open('out.bin', "wb") as out:
        out.close()

    with open(argv[1]) as f:
        for line in f:
            if line[0] in ';.':
                continue

            line = line.replace('\n', '').replace('\r', '')
            token = re.split(r'[, ]', line)

            match token[0].upper():
                case "NOP":
                    b = make_instruction(Instructions.NOP, Mode.IMP)
                    write_out(b)
                case "LDA":
                    value = token[1]
                    match value[0]:
                        case "#":
                            b = make_instruction(Instructions.LDI, Mode.IMM, value)
                            write_out(b)
                        case "$":
                            b = make_instruction(Instructions.LDA, Mode.IMP, value)
                            write_out(b)
                case "STA":
                    value = token[1]
                    match value[0]:
                        case "$":
                            b = make_instruction(Instructions.STA, Mode.IMP, value)
                            write_out(b)
                case "ADD":
                    value = token[1]
                    match value[0]:
                        case "#":
                            b = make_instruction(Instructions.ADD, Mode.IMM, value)
                            write_out(b)
                        case "$":
                            b = make_instruction(Instructions.ADA, Mode.IMP, value)
                            write_out(b)
                case "SUB":
                    value = token[1]
                    match value[0]:
                        case "#":
                            b = make_instruction(Instructions.SUB, Mode.IMM, value)
                            write_out(b)
                        case "$":
                            b = make_instruction(Instructions.SUA, Mode.IMP, value)
                            write_out(b)
                case "MUL":
                    value = token[1]
                    match value[0]:
                        case "#":
                            b = make_instruction(Instructions.MUL, Mode.IMM, value)
                            write_out(b)
                        case "$":
                            b = make_instruction(Instructions.MUA, Mode.IMP, value)
                            write_out(b)
                case "DIV":
                    value = token[1]
                    match value[0]:
                        case "#":
                            b = make_instruction(Instructions.DIV, Mode.IMM, value)
                            write_out(b)
                        case "$":
                            b = make_instruction(Instructions.DIA, Mode.IMP, value)
                            write_out(b)
                case "MOD":
                    value = token[1]
                    match value[0]:
                        case "#":
                            b = make_instruction(Instructions.MOD, Mode.IMM, value)
                            write_out(b)
                        case "$":
                            b = make_instruction(Instructions.MOA, Mode.IMP, value)
                            write_out(b)
                case "HLT":
                    b = make_instruction(Instructions.HLT, Mode.IMP)
                    write_out(b)
                    pass

if __name__ == '__main__':
    if len(argv) < 2:
        usage(argv[0])
    else:
        main()

