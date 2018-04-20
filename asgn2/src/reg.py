import sys
from parser import parser

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
        self.asm = ''

    def condition_1_2(self, var1, address_descriptor, nextUseList, var2=None):
        self.asm = ''
        for k, v in self.regdict.items():
            if var1 == v:
                return True

        for k, v in self.regdict.items():
            if v == var2 and var2 not in nextUseList.keys():
                self.asm = 'movl ' + k + ', ' +  var2 + '\n'
                self.asm += 'movl (' + var1 + '), ' + k + '\n'
                self.regdict[k] = var1
                address_descriptor[var1] = k
                address_descriptor[var2] = var2
                return True
            elif not v:
                self.asm = 'movl (' + var1 + '), ' + k + '\n' 
                self.regdict[k] = var1
                address_descriptor[var1] = k
                return True
        return False

    # If ccondition 1 and 2 fail, var1 has a next use
    def condition_3(self, var1, lineno, blockNextUseTable, address_descriptor):
        best_k = ''
        best_v = ''
        latest = -1
        nextUseList = blockNextUseTable[lineno]
        if var1 not in nextUseList.keys():
            return ''
        for k, v in self.regdict.items():
            if v in nextUseList.keys():
                if nextUseList[v] > latest:
                    best_v = v
                    best_k = k
                    latest = nextUseList[v]
            else:
                best_v = v
                best_k = k
                break

        asm = ''
        asm += 'movl ' + best_k + ', ' + best_v + '\n'
        self.regdict[best_k] = var1
        address_descriptor[var1] = best_k
        address_descriptor[best_v] = best_v
        return asm

    def condition_4(self, var1, address_descriptor):
        address_descriptor[var1] = var1

    # Assigns register for a given variable
    def getRegister(self, var, address_descriptor, nextUseList, usedlist=[]):
        latest = 0
        best_k = ''
        best_v = ''
        if len(usedlist) > 3:
            print(" Error, trying to use more than 4 variables in a line")
            exit()
        if var in self.regdict.values():
            return address_descriptor, ''
        # nextUseList = blockNextUseTable[lineno]
        for k, v in self.regdict.items():
            if v:
                if v in usedlist:
                    continue
                elif v in nextUseList.keys():
                    if nextUseList[v] > latest:
                        best_v = v
                        best_k = k
                        latest = nextUseList[v]
                else:
                    asm = 'movl ' + k + ', ' + v + '\n'
                    asm += 'movl (' + var + '), ' + k + '\n'
                    self.regdict[k] = var
                    address_descriptor[var] = k
                    address_descriptor[v] = v
                    return address_descriptor, asm
            else:
                asm = 'movl (' + var + '), ' + k + '\n'
                # asm += 'movl (' + var + '), ' + k + '\n'
                self.regdict[k] = var
                address_descriptor[var] = k
                return address_descriptor, asm

        asm = ''
        asm += 'movl ' + best_k + ', ' + best_v + '\n'
        asm += 'movl (' + var + '), ' + best_k + '\n'
        self.regdict[best_k] = var
        address_descriptor[var] = best_k
        address_descriptor[best_v] = best_v

        return address_descriptor, asm

    def getReg(self,blockNextUseTable, instr, address_descriptor, variable_list, var=None):
        asm = ''
        self.asm = ''
        parsed = parser(instr, variable_list)

        if parsed["op"]  == 'fn_def':
            usedlist = []
        else:
            usedlist = parsed["used"]

        if(var):
            v = var
        else:
            v = parsed['killed'][0]
        if v:
            address_descriptor, asm = self.getRegister(v, address_descriptor, blockNextUseTable[int(instr[0])], usedlist= usedlist)
        #     if not parsed['used']:
        #         if not self.condition_1_2(v,address_descriptor,blockNextUseTable[int(instr[0])]):
        #             asm = self.condition_3(v, int(instr[0]), blockNextUseTable, address_descriptor)
        #             if not (asm):
        #                 self.condition_4(v,address_descriptor)
        #     else:
        #         if not self.condition_1_2(v, address_descriptor, blockNextUseTable[int(instr[0])], parsed["used"][0]):
        #             asm = self.condition_3(v, int(instr[0]), blockNextUseTable, address_descriptor)
        #             if not (asm):
        #                 self.condition_4(v,address_descriptor)
        #                 self.asm += "###----\n"
        #             else:
        #                 self.asm += "###---\n"
        #         else:
        #             self.asm += "###-/--\n"

        if self.asm:
            asm = self.asm
            self.asm = ''

        return address_descriptor, asm
