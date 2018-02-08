import sys

class Reg:
    def __init__(self, regAlloc = None):
        self.regdict = {}
        if regAlloc is not None:
            self.regdict = dict(regAlloc)
        else:
            self.regdict = {
                'rax': "",
                'rbx': "",
                'rcx': "",
                'rdx': "",
            }

    def getReg(blockNextUseTable, instr):
        instr = instr.split(', ')

