class table:
    def __init__(self, previous = None):
        self.parent = previous # None means the start
        self.children = []
        self.entries = {}
        self.labels = {}
        self.keywords()
        # Add list of all keywords
        self.keywords_list = ['print', 'scan', 'int', 'abstract']
    
    def enter_var(self, name, Dtype, arr=None):
        self.entries[name] = {}
        self.entries[name]['type'] = Dtype
        self.entries[name]['category'] = 'var'
        if(arr):
            self.entries[name]['category'] = 'arr'

    def enter_temp_var(self, Dtype):
        i = 0
        flag = False
        while(not flag):
            i+=1
            tname = 'temp' + str(i)
            if tname not in self.entries:
                flag = True
                self.entries[tname] = {}
                self.entries[tname]['type'] = Dtype
                self.entries[tname]['category'] = 'temp_var'
        return tname

    def enter_function(self, method_name, return_type, param_types):
		if method_name not in self.entries:
			self.entries[method_name] = {}
			self.entries[method_name]['type'] = return_type
			self.entries[method_name]['category'] = 'function'
			self.entries[method_name]['arg_types'] = param_types
			self.entries[method_name]['arg_num'] = len(param_types)

    def lookup(self, name):
        if name in self.entries:
            return True
        else:
            return False
    
    def keywords(self):
        for kw in self.keywords_list:
            self.entries[kw] = {}
            self.entries[kw]['category'] = 'keyword'

class environment:
    def __init__(self):
        self.global_env = table()
        self.pres_env = self.global_env
        self.label_count = 0
    
    def mklabel(self):
        label_name = 'l' + str(self.label_count)
        self.label_count +=1
        self.pres_env.labels[label_name] = {}
        self.pres_env.labels[label_name]['category'] = 'label'
        return label_name

    def new_scope(self):
		new_env = table(self.pres_env)
		self.pres_env.children.append(new_env)
		self.pres_env = new_env
		# return self.pres_env
    
    def close_scope(self):
		self.pres_env = self.pres_env.parent
        # return self.pres_env

    def global_lookup(self,name,env):
        if env is None:
            return False
        else:
            flag = env.lookup(name)
            if(not flag):
                return self.global_lookup(name,env.parent)
            else:
                return True