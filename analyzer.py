from parser import parser
from lexer import lexer

def analyze(file_name: str) -> str:
    with open(file_name, 'r') as f:
        ret = parser.parse(lexer.tokenize(f.read()))
    return ret