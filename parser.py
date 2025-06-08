from sly import Parser

from lexer import ObsActLexer

class ObsActParser(Parser):
    debugfile = "parser.out"
    tokens = ObsActLexer.tokens

    def error(self, t):
        return f"Syntax error at line {t.lineno}, token={t.type}"

parser = ObsActParser()