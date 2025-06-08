from sly import Lexer

class ObsActLexer(Lexer):
    ignore = " \t"

    tokens = []

    def error(self, t):
        print(f"Lexer error at '{t.value}'")
        self.index += 1

lexer = ObsActLexer()