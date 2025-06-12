from sly import Lexer

class ObsActLexer(Lexer):
    ignore = " \t\n"

    boolean = r'True|False'
    number = r'\d+'
    device = r'dispositivo'
    set = r'set'
    action = r'ligar|desligar'

    namedevice = r'[A-Z][a-zA-Z0-9]*'
    observation = r'[a-z][a-zA-Z0-9]*'

    literals = {'{', '}', ',', ':', '=', '.'}

    tokens = ["device", "set", "boolean", "number", "action", "namedevice", "observation", ]

    def __init__(self):
        self.nesting_level = 0

    @_(r'\{')
    def lbrace(self, t):
        t.type = '{'  # Set token type to the expected literal
        self.nesting_level += 1
        return t

    @_(r'\}')
    def rbrace(self, t):
        t.type = '}'  # Set token type to the expected literal
        self.nesting_level -= 1
        return t

    def error(self, t):
        print(f"Lexer error at '{t.value}'")
        self.index += 1

lexer = ObsActLexer()