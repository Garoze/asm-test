#!/usr/bin/env python3

# Reference:
# https://github.com/garyexplains/examples/blob/master/vASM.py

import re
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

def usage(program):
    print(f"usage: {program} <file_path>")
    exit(1)

def write_out(b):
    print(bytearray(b))
    #  with open("out.bin", "ab") as out:
    #      out.write(bytearray(b))

def main():
    with open(argv[1]) as f:
        for line in f:
            if line[0] in ';.':
                continue

            line = line.replace('\n', '').replace('\r', '')
            token = re.split(r'[, ]', line)

            match token[0].upper():
                case "NOP":
                    pass
                case "LDA":
                    value = token[1]
                    match value[0]:
                        case "#":
                            imm16 = int(f'0x{value[1:]}', 16)
                            b = [Instructions.LDI, (imm16 & 0x00FF), (imm16 & 0xFF00) >> 8]
                            write_out(b)
                        case "$":
                            add16 = int(f'0x{value[1:]}', 16)
                            b = [Instructions.LDA, (add16 & 0x00FF), (add16 & 0xFF00) >> 8]
                            write_out(b)
                case "STA":
                    value = token[1]
                    match value[0]:
                        case "$":
                            add16 = int(f'0x{value[1:]}', 16)
                            b = [Instructions.STA, (add16 & 0x00FF), (add16 & 0xFF00) >> 8]
                            write_out(b)
                case "ADD":
                    value = token[1]
                    match value[0]:
                        case "#":
                            imm16 = int(f'0x{value[1:]}', 16)
                            b = [Instructions.ADD, (imm16 & 0x00FF), (imm16 & 0xFF00) >> 8]
                            write_out(b)
                        case "$":
                            add16 = int(f'0x{value[1:]}', 16)
                            b = [Instructions.ADA, (add16 & 0x00FF), (add16 & 0xFF00) >> 8]
                            write_out(b)
                case "SUB":
                    value = token[1]
                    match value[0]:
                        case "#":
                            imm16 = int(f'0x{value[1:]}', 16)
                            b = [Instructions.SUB, (imm16 & 0x00FF), (imm16 & 0xFF00) >> 8]
                            write_out(b)
                        case "$":
                            add16 = int(f'0x{value[1:]}', 16)
                            b = [Instructions.SUA, (add16 & 0x00FF), (add16 & 0xFF00) >> 8]
                            write_out(b)
                case "MUL":
                    value = token[1]
                    match value[0]:
                        case "#":
                            imm16 = int(f'0x{value[1:]}', 16)
                            b = [Instructions.MUL, (imm16 & 0x00FF), (imm16 & 0xFF00) >> 8]
                            write_out(b)
                        case "$":
                            add16 = int(f'0x{value[1:]}', 16)
                            b = [Instructions.MUA, (add16 & 0x00FF), (add16 & 0xFF00) >> 8]
                            write_out(b)
                case "DIV":
                    value = token[1]
                    match value[0]:
                        case "#":
                            imm16 = int(f'0x{value[1:]}', 16)
                            b = [Instructions.DIV, (imm16 & 0x00FF), (imm16 & 0xFF00) >> 8]
                            write_out(b)
                        case "$":
                            add16 = int(f'0x{value[1:]}', 16)
                            b = [Instructions.DIA, (add16 & 0x00FF), (add16 & 0xFF00) >> 8]
                            write_out(b)
                case "MOD":
                    value = token[1]
                    match value[0]:
                        case "#":
                            imm16 = int(f'0x{value[1:]}', 16)
                            b = [Instructions.MOD, (imm16 & 0x00FF), (imm16 & 0xFF00) >> 8]
                            write_out(b)
                        case "$":
                            add16 = int(f'0x{value[1:]}', 16)
                            b = [Instructions.MOA, (add16 & 0x00FF), (add16 & 0xFF00) >> 8]
                            write_out(b)
                case "HLT":
                    b  = [Instructions.HLT]
                    write_out(b)
                    pass


if __name__ == '__main__':
    if len(argv) < 2:
        usage(argv[0])
    else:
        main()

