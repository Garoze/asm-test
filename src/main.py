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
    #  STA = auto()
    #  STS = auto()
    #  ADD = auto()
    #  ADA = auto()
    #  ADS = auto()
    #  SUB = auto()
    #  SUA = auto()
    #  SUS = auto()
    #  MUL = auto()
    #  MUA = auto()
    #  MUS = auto()
    #  DIV = auto()
    #  DIA = auto()
    #  DIS = auto()
    #  MOD = auto()
    #  MOA = auto()
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
    #  HLT = auto()

def usage(program):
    print(f"usage: {program} <file_path>")
    exit(1)

def write_out(b):
    print(bytearray(b))
    #  with open("out.bin", "ab") as out:
    #      out.write(bytearray(b))

def main():
    PC = 0x0000
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
                case "HLT":
                    pass


if __name__ == '__main__':
    if len(argv) < 2:
        usage(argv[0])
    else:
        main()

