from opcodes import Instructions, Modes, Address

Opcode_t = {
    "NOP": {
        "_": (Instructions.NOP, Modes.IMP),
    },
    "LDA": {
        "#": (Instructions.LDI, Modes.IMM, Address.I16),
        "$": (Instructions.LDA, Modes.ABS, Address.I16),
        "_": (Instructions.LDS, Modes.IMP),
    },
    "STA": {
        "$": (Instructions.STA, Modes.ABS, Address.I16),
    },
    "STS": {
        "$": (Instructions.STS, Modes.ABS, Address.I16),
    },
    "ADD": {
        "#": (Instructions.ADD, Modes.IMM, Address.I16),
        "$": (Instructions.ADA, Modes.ABS, Address.I16),
        "_": (Instructions.ADS, Modes.IMP),
    },
    "SUB": {
        "#": (Instructions.SUB, Modes.IMM, Address.I16),
        "$": (Instructions.SUA, Modes.ABS, Address.I16),
        "_": (Instructions.SUS, Modes.IMP),
    },
    "MUL": {
        "#": (Instructions.MUL, Modes.IMM, Address.I16),
        "$": (Instructions.MUA, Modes.ABS, Address.I16),
        "_": (Instructions.MUS, Modes.IMP),
    },
    "DIV": {
        "#": (Instructions.DIV, Modes.IMM, Address.I16),
        "$": (Instructions.DIA, Modes.ABS, Address.I16),
        "_": (Instructions.DIS, Modes.IMP),
    },
    "MOD": {
        "#": (Instructions.MOD, Modes.IMM, Address.I16),
        "$": (Instructions.MOA, Modes.ABS, Address.I16),
        "_": (Instructions.MOS, Modes.IMP),
    },
    "INC": {
        "_": (Instructions.INC, Modes.IMP),
    },
    "DEC": {
        "_": (Instructions.DEC, Modes.IMP),
    },
    "SHL": {
        "#": (Instructions.SHL, Modes.IMM, Address.IM8),
    },
    "SHR": {
        "#": (Instructions.SHR, Modes.IMM, Address.IM8),
    },
    "AND": {
        "#": (Instructions.AND, Modes.IMM, Address.I16),
    },
    "BOR": {
        "#": (Instructions.BOR, Modes.IMM, Address.I16),
    },
    "XOR": {
        "#": (Instructions.XOR, Modes.IMM, Address.I16),
    },
    "NOT": {
        "_": (Instructions.NOT, Modes.IMP),
    },
    "PSH": {
        "#": (Instructions.PSH, Modes.IMM, Address.I16),
    },
    "POP": {
        "_": (Instructions.POP, Modes.IMP),
    },
    "CMP": {
        "#": (Instructions.CMP, Modes.IMM, Address.I16),
        "$": (Instructions.CMA, Modes.ABS, Address.I16),
        "_": (Instructions.CMS, Modes.IMP),
    },
    "JMP": {
        "$": (Instructions.JMP, Modes.ABS, Address.I16),
        "L": (Instructions.JMP, Modes.LBE, Address.I16),
    },
    "JMZ": {
        "$": (Instructions.JMZ, Modes.ABS, Address.I16),
        "L": (Instructions.JMP, Modes.LBE, Address.I16),
    },
    "JNZ": {
        "$": (Instructions.JNZ, Modes.ABS, Address.I16),
        "L": (Instructions.JNZ, Modes.LBE, Address.I16),
    },
    "CAL": {
        "$": (Instructions.CAL, Modes.ABS, Address.I16),
        "L": (Instructions.CAL, Modes.LBE, Address.I16),
    },
    "RET": {
        "_": (Instructions.RET, Modes.IMP),
    },
    "OUT": {
        "_": (Instructions.OUT, Modes.IMP),
    },
    "HLT": {
        "_": (Instructions.HLT, Modes.IMP),
    }
}

