from parser import ObsActParser
from lexer import ObsActLexer

lexer = ObsActLexer()
parser = ObsActParser()

def test_Lexer_dispositivos():
    test_tokenize = "dispositivo:{Termometro}\n dispositivo:{Batata, temperatura}"
    res = lexer.tokenize(test_tokenize)
    for tok in res:
        print('type=%r, value=%r' % (tok.type, tok.value))
    return True

def test_Parser_dispositivos():
    test_tokenize = "dispositivo:{Termometro}\n dispositivo:{Batata, temperatura}"
    res = parser.parse(lexer.tokenize(test_tokenize))
    print(res)
    return True

def test_Lexer_attrib():
    test_tokenize = "dispositivo:{Batata, temperatura}\n set temperatura = True."
    res = lexer.tokenize(test_tokenize)
    for tok in res:
        print('type=%r, value=%r' % (tok.type, tok.value))
    return True

def test_Parser_attrib():
    test_tokenize = "dispositivo:{Batata, temperatura}\n set temperatura = 1000."
    res = parser.parse(lexer.tokenize(test_tokenize))
    print(res)
    return True

def test_Lexer_act():
    test_tokenize = "dispositivo:{Batata}\n ligar Batata."
    res = lexer.tokenize(test_tokenize)
    for tok in res:
        print('type=%r, value=%r' % (tok.type, tok.value))
    return True

def test_Parser_act():
    test_tokenize = "dispositivo:{Batata}\n ligar Batata."
    res = parser.parse(lexer.tokenize(test_tokenize))
    print(res)
    return True

if __name__ == '__main__':
    test_Lexer_dispositivos()
    test_Parser_dispositivos()
    test_Lexer_attrib()
    test_Parser_attrib()
    test_Lexer_act()
    test_Parser_act()