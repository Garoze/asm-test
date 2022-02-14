from enum import IntFlag, auto

class Modes(IntFlag):
    IMP = auto()
    IMM = auto()
    ABS = auto()
    LBE = auto()

class Address(IntFlag):
    IM8 = auto()
    I16 = auto()

class Instructions(IntFlag):
    NOP = 0x00
    LDI = 0x01
    LDA = 0x02
    LDS = 0x03
    STA = 0x04
    STS = 0x05
    ADD = 0x06
    ADA = 0x07
    ADS = 0x08
    SUB = 0x09
    SUA = 0x0A
    SUS = 0x0B
    MUL = 0x0C
    MUA = 0x0D
    MUS = 0x0E
    DIV = 0x0F
    DIA = 0x10
    DIS = 0x11
    MOD = 0x12
    MOA = 0x13
    MOS = 0x14
    INC = 0x15
    DEC = 0x16
    SHL = 0x17
    SHR = 0x18
    AND = 0x19
    BOR = 0x1A
    XOR = 0x1B
    NOT = 0x1C
    PSH = 0x1D
    POP = 0x1E
    CMP = 0x1F
    CMA = 0x20
    CMS = 0x21
    JMP = 0x22
    JMZ = 0x23
    JNZ = 0x24
    CAL = 0x25
    RET = 0x26
    OUT = 0x27
    HLT = 0x28

