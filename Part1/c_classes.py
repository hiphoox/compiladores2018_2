class Int_kw:
    def __init__(self):
        self.kw = "int"

class Id_kw:
    def __init__(self, id):
        self.id = id

class Open_paren:
    def __init__(self):
        self.paren = "("

class Close_paren:
    def __init__(self):
        self.paren = ")"
    
class Open_brace:
    def __init__(self):
        self.brace = "{"

class Close_brace:
    def __init__(self):
        self.brace = "}"

class Ret_kw:
    def __init__(self):
        self.kw = "return"

class Literal_num:
    def __init__(self, num):
        self.num = num

class Semicolon:
    def __init__(self):
        self.semi = ";"
