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

def test_Lexer_alert():
    test_tokenize = "dispositivo:{Batata}\n enviar alerta (\"Muito caliente\") Batata."
    res = lexer.tokenize(test_tokenize)
    for tok in res:
        print('type=%r, value=%r' % (tok.type, tok.value))
    return True

def test_Parser_alert():
    test_tokenize = "dispositivo:{Batata}\n enviar alerta (\"Muito caliente\") Batata."
    res = parser.parse(lexer.tokenize(test_tokenize))
    print(res)
    return True

def test_Lexer_alert_observation():
    test_tokenize = "dispositivo:{Batata, temperatura}\nset temperatura = 100.\nenviar alerta (\"Muito caliente, está à \", temperatura) Batata."
    res = lexer.tokenize(test_tokenize)
    for tok in res:
        print('type=%r, value=%r' % (tok.type, tok.value))
    return True

def test_Parser_alert_observation():
    test_tokenize = "dispositivo:{Batata, temperatura}\nset temperatura = 100.\nenviar alerta (\"Muito caliente, está à \", temperatura) Batata."
    res = parser.parse(lexer.tokenize(test_tokenize))
    print(res)
    return True

def test_Lexer_alert_all():
    test_tokenize = "dispositivo:{Batata}\ndispositivo:{Cebola}\n enviar alerta (\"Sopa\") para todos: Batata, Cebola."
    res = lexer.tokenize(test_tokenize)
    for tok in res:
        print('type=%r, value=%r' % (tok.type, tok.value))
    return True

def test_Parser_alert_all():
    test_tokenize = "dispositivo:{Batata}\ndispositivo:{Cebola}\n enviar alerta (\"Sopa\") para todos: Batata, Cebola."
    res = parser.parse(lexer.tokenize(test_tokenize))
    print(res)
    return True

def test_Lexer_obsact_if():
    test_tokenize = "dispositivo:{Batata, temperatura}\nset temperatura = 100.\nse temperatura >= 90 entao enviar alerta (\"Muito caliente, está à \", temperatura) Batata."
    res = lexer.tokenize(test_tokenize)
    for tok in res:
        print('type=%r, value=%r' % (tok.type, tok.value))
    return True

def test_Parser_obsact_if():
    test_tokenize = "dispositivo:{Batata, temperatura}\nset temperatura = 100.\nse temperatura >= 90 entao enviar alerta (\"Muito caliente, está à \", temperatura) Batata."
    res = parser.parse(lexer.tokenize(test_tokenize))
    print(res)
    return True

def test_Lexer_obsact_if_else():
    test_tokenize = "dispositivo:{Batata, temperatura}\nset temperatura = 100.\nse temperatura >= 90 entao enviar alerta (\"Muito caliente, está à \", temperatura) Batata senao desligar Batata."
    res = lexer.tokenize(test_tokenize)
    for tok in res:
        print('type=%r, value=%r' % (tok.type, tok.value))
    return True

def test_Parser_obsact_if_else():
    test_tokenize = "dispositivo:{Batata, temperatura}\nset temperatura = 100.\nse temperatura >= 90 entao enviar alerta (\"Muito caliente, está à \", temperatura) Batata senao desligar Batata."
    res = parser.parse(lexer.tokenize(test_tokenize))
    print(res)
    return True

def test_Lexer_obsact_observations():
    test_tokenize = "dispositivo:{Batata, temperatura}\nset temperatura = 100.\nse temperatura >= 90 && temperatura < 1000 entao enviar alerta (\"Muito caliente, está à \", temperatura) Batata."
    res = lexer.tokenize(test_tokenize)
    for tok in res:
        print('type=%r, value=%r' % (tok.type, tok.value))
    return True

def test_Parser_obsact_observations():
    test_tokenize = "dispositivo:{Batata, temperatura}\nset temperatura = 100.\nse temperatura >= 90 && temperatura < 1000 entao enviar alerta (\"Muito caliente, está à \", temperatura) Batata."
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
    test_Lexer_alert()
    test_Parser_alert()
    test_Lexer_alert_observation()
    test_Parser_alert_observation()
    test_Lexer_alert_all()
    test_Parser_alert_all()
    test_Lexer_obsact_if()
    test_Parser_obsact_if()
    test_Lexer_obsact_if_else()
    test_Parser_obsact_if_else()
    test_Lexer_obsact_observations()
    test_Parser_obsact_observations()