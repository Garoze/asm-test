from opcodes import Instructions, Modes, Address

Opcode_t = {
    "NOP": (Instructions.NOP, Modes.IMP),
    "LDI": (Instructions.LDI, Modes.IMM, Address.I16),
    "LDA": (Instructions.LDA, Modes.IMM, Address.I16),
    "HLT": (Instructions.HLT, Modes.IMP),
}

