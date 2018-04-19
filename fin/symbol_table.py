#!/usr/bin/env python3
from copy import deepcopy

class type:
    def __init__(self, name, isbasic, isarray, length, data_width, arr_elem_type):
        self.dict = {}
        self.dict['name'] = name
        self.dict['isbasic'] = isbasic
        self.dict['isarray'] = isarray
        # self.dict['ispointer'] = ispointer
        self.dict['data_width'] = data_width # int is 4, char is 1  ....
        self.dict['arr_elem_type'] = arr_elem_type
        self.dict['length'] = length

    def type_name(self):
        if self.dict['isbasic']:
            return self.dict['name']
        elif self.dict['isarray']:
            return "array of " + self.dict['arr_elem_type'].type_name() + ", length " + str(self.dict['length'])

class table:
    def __init__(self, previous = None):
        self.parent = previous # None means the start
        self.children = []
        self.entries = {}
        self.labels = {}
        self.keywords_list = ['print', 'scan', 'int', 'abstract']
        self.keywords()
        self.is_func_table = False
        self.number = 0
        # Add list of all keywords

    def enter_var(self, name, Dtype, arr=None, tmp=False):
        self.entries[name] = {}
        self.entries[name]['type'] = Dtype
        self.entries[name]['category'] = 'var'
        self.entries[name]['tab_no'] = deepcopy(self.number)
        if(arr):
            self.entries[name]['category'] = 'arr'
        elif tmp:
            self.entries[name]['category'] = 'temp'

    def enter_function(self, method_name, return_type, param_types, class_name = ""):
        if method_name not in self.entries:
            self.entries[method_name] = {}
            self.entries[method_name]['type'] = return_type
            self.entries[method_name]['category'] = 'function'
            self.entries[method_name]['arg_types'] = param_types
            self.entries[method_name]['arg_num'] = len(param_types)
            self.entries[method_name]['class_name'] = class_name

    def lookup(self, name):
        if name in self.entries.keys():
            return self.entries[name]
        else:
            return None

    def keywords(self):
        for kw in self.keywords_list:
            self.entries[kw] = {}
            self.entries[kw]['category'] = 'keyword'

    def print_symbol_table(self):
        for key in self.entries:
            print("NAME: ", key)
            for k in self.entries[key]:
                if k == 'type' and not isinstance(self.entries[key][k], str):
                    print(k, ': ', self.entries[key][k].type_name())
                elif k == 'arg_types':
                    types = []
                    for t in self.entries[key][k]:
                        if not isinstance(t, str):
                            types.append(t.type_name())
                        else:
                            types.append(t)
                    print(k, ': ', types)
                else:
                    print(k, ': ', self.entries[key][k])

class environment:
    def __init__(self):
        self.global_env = table()
        self.pres_env = self.global_env
        self.label_count = 0
        self.temp_count = 0
        self.table_count = 1
        self.global_env.number = self.table_count

    def mklabel(self):
        label_name = 'l' + str(self.label_count)
        self.label_count +=1
        self.pres_env.labels[label_name] = {}
        self.pres_env.labels[label_name]['category'] = 'label'
        return label_name

    def mktemp(self, Dtype):
        self.temp_count += 1
        temp_name = 't' + str(self.temp_count)
        while self.prev_lookup(temp_name, self.pres_env):
            self.temp_count += 1
            temp_name = 't' + str(self.temp_count)

        self.pres_env.enter_var(temp_name, Dtype, tmp=True)
        return temp_name

    def new_scope(self):
        new_env = table(self.pres_env)
        self.pres_env.children.append(new_env)
        self.pres_env = new_env
        self.table_count += 1
        self.pres_env.number = deepcopy(self.table_count)
        return self.pres_env

    def close_scope(self):
        self.pres_env = self.pres_env.parent
        # return self.pres_env

    def prev_lookup(self, name, env):
        # print(env)
        if env is None:
            return False
        else:
            var = env.lookup(name)
            if env.is_func_table:
                if var is None:
                    return False
                else:
                    return var
            if(var is None):
                # print('boo')
                # print(env.parent.print_symbol_table())
                return self.prev_lookup(name, env.parent)
            else:
                return var

    def print_symbol_table(self, t):
        t.print_symbol_table()
        print("----------------")
        for c in t.children:
            print('noooo')
            self.print_symbol_table(c)
