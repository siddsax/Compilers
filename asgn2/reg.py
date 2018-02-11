import sys
from parser import parser

# TODO: Check next use of variable which is being given a new value

class Reg:
    def __init__(self, regAlloc = None):
        self.regdict = {}
        if regAlloc is not None:
            self.regdict = dict(regAlloc)
        else:
            self.regdict = {
                '%eax': "",
                '%ebx': "",
                '%ecx': "",
                '%edx': "",
            }

    def condition_1_2(self, var1, address_descriptor, var2=None):
        for k, v in self.regdict.items():
            if var1 == v:
                return True
        for k, v in self.regdict.items():
            if v == var2:
                self.regdict[k] = var1
                address_descriptor[var1] = k
                return True
            elif not v:
                self.regdict[k] = var1
                address_descriptor[var1] = k
                return True
        return False;

    def condition_3(self, var1, lineno, blockNextUseTable, address_descriptor):
        best_k = ''
        best_v = ''
        latest = 0
        for k, v in self.regdict.items():
            nextUseList = blockNextUseTable[lineno]
            print(nextUseList)
            if v in nextUseList.keys():
                if nextUseList[v] > latest:
                    best_v = v
                    best_k = k
                    latest = nextUseList[v]

        # TODO: Write code to save value of ejected variable in memory
        asm = ''
        asm += 'movl ' + best_k + ', ' + best_v + '\n'
        self.regdict[best_k] = var1
        address_descriptor[var1] = best_k
        address_descriptor[best_v] = var1
        return asm

    def condition_4(self, var1, address_descriptor):
        # TODO: Save var1 to memory
        address_descriptor[var1] = var1

    # Assigns register for a given variable
    def getRegister(self, var, address_descriptor, blockNextUseTable, lineno):
        latest = 0
        best_k = ''
        best_v = ''
        for reg, v in self.regdict.items():
            if v:
                nextUseList = blockNextUseTable[lineno]
                if v in nextUseList.keys():
                    if nextUseList[v] > latest:
                        best_v = v
                        best_k = k
                        latest = nextUseList[v]
                else:
                    self.regdict[k] = var1
                    address_descriptor[var1] = k
            else:
                self.regdict[k] = var
                address_descriptor[var] = k
                return address_descriptor

        asm = ''
        asm += 'movl ' + best_k + ', ' + best_v + '\n'
        asm += 'movl (' + var + '), ' + best_k + '\n'
        self.regdict[best_k] = var
        address_descriptor[var] = best_k
        address_descriptor[best_v] = "$" + var

        return address_descriptor, asm

    def getReg(self,blockNextUseTable, instr, address_descriptor, variable_list):
        asm = ''
        # instr = instr.split(', ')
        parsed = parser(instr, variable_list)
        if parsed['killed']:
            if not parsed['used']:
                if not self.condition_1_2(parsed["killed"][0],address_descriptor):
                    asm = self.condition_3(parsed["killed"][0], int(instr[0]), blockNextUseTable, address_descriptor)
                    if not (asm):
                        self.condition_4(parsed["killed"][0],address_descriptor)
            else:
                if not self.condition_1_2(parsed["killed"][0], address_descriptor, parsed["used"][0]):
                    asm = self.condition_3(parsed["killed"][0], int(instr[0]), blockNextUseTable, address_descriptor)
                    if not (asm):
                        self.condition_4(parsed["killed"][0],address_descriptor)

        return address_descriptor, asm
