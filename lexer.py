from sly import Lexer
from sly.lex import LexError


class ObsActLexer(Lexer):
    ignore = " \t\n"

    boolean = r'True|False'
    number = r'\d+'
    device = r'dispositivo'
    set = r'set'
    enviar = r'enviar'
    alerta = r'alerta'
    para = r'para'
    todos = r'todos'
    senao = r'senao'
    se = r'se'
    entao = r'entao'
    action = r'ligar|desligar'

    oplogic = r'==|!=|>=|<=|>|<'
    namedevice = r'[A-Z][a-zA-Z0-9]*'
    observation = r'[a-z][a-zA-Z0-9]*'
    msg = r'"([\s\S]*?)"'

    literals = {'{', '}', '(', ')', ',', ':', '=', '.', '&'}

    tokens = ["device", "set", "enviar", "alerta", "para", "todos", "se", "entao", "senao", "boolean", "number", "action", "msg", "oplogic", "namedevice", "observation", ]

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
        raise LexError('Line %d: Bad character %r' % (self.lineno, t.value[0]), t.value, self.index)

lexer = ObsActLexer()