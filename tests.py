from parser import ObsActParser
from lexer import ObsActLexer

lexer = ObsActLexer()
parser = ObsActParser()

ans_Lexer = [
"""type='device', value='dispositivo'
type=':', value=':'
type='{', value='{'
type='namedevice', value='Termometro'
type='}', value='}'
type='device', value='dispositivo'
type=':', value=':'
type='{', value='{'
type='namedevice', value='Batata'
type=',', value=','
type='observation', value='temperatura'
type='}', value='}'
""",

"""type='device', value='dispositivo'
type=':', value=':'
type='{', value='{'
type='namedevice', value='Batata'
type=',', value=','
type='observation', value='temperatura'
type='}', value='}'
type='set', value='set'
type='observation', value='temperatura'
type='=', value='='
type='boolean', value='True'
type='.', value='.'
""",

"""type='device', value='dispositivo'
type=':', value=':'
type='{', value='{'
type='namedevice', value='Batata'
type='}', value='}'
type='action', value='ligar'
type='namedevice', value='Batata'
type='.', value='.'
""",

"""type='device', value='dispositivo'
type=':', value=':'
type='{', value='{'
type='namedevice', value='Batata'
type='}', value='}'
type='enviar', value='enviar'
type='alerta', value='alerta'
type='(', value='('
type='msg', value='"Muito caliente"'
type=')', value=')'
type='namedevice', value='Batata'
type='.', value='.'
""",

"""type='device', value='dispositivo'
type=':', value=':'
type='{', value='{'
type='namedevice', value='Batata'
type=',', value=','
type='observation', value='temperatura'
type='}', value='}'
type='set', value='set'
type='observation', value='temperatura'
type='=', value='='
type='number', value='100'
type='.', value='.'
type='enviar', value='enviar'
type='alerta', value='alerta'
type='(', value='('
type='msg', value='"Muito caliente, está à "'
type=',', value=','
type='observation', value='temperatura'
type=')', value=')'
type='namedevice', value='Batata'
type='.', value='.'
""",

"""type='device', value='dispositivo'
type=':', value=':'
type='{', value='{'
type='namedevice', value='Batata'
type='}', value='}'
type='device', value='dispositivo'
type=':', value=':'
type='{', value='{'
type='namedevice', value='Cebola'
type='}', value='}'
type='enviar', value='enviar'
type='alerta', value='alerta'
type='(', value='('
type='msg', value='"Sopa"'
type=')', value=')'
type='para', value='para'
type='todos', value='todos'
type=':', value=':'
type='namedevice', value='Batata'
type=',', value=','
type='namedevice', value='Cebola'
type='.', value='.'
""",

"""type='device', value='dispositivo'
type=':', value=':'
type='{', value='{'
type='namedevice', value='Batata'
type=',', value=','
type='observation', value='temperatura'
type='}', value='}'
type='set', value='set'
type='observation', value='temperatura'
type='=', value='='
type='number', value='100'
type='.', value='.'
type='se', value='se'
type='observation', value='temperatura'
type='oplogic', value='>='
type='number', value='90'
type='entao', value='entao'
type='enviar', value='enviar'
type='alerta', value='alerta'
type='(', value='('
type='msg', value='"Muito caliente, está à "'
type=',', value=','
type='observation', value='temperatura'
type=')', value=')'
type='namedevice', value='Batata'
type='.', value='.'
""",

"""type='device', value='dispositivo'
type=':', value=':'
type='{', value='{'
type='namedevice', value='Batata'
type=',', value=','
type='observation', value='temperatura'
type='}', value='}'
type='set', value='set'
type='observation', value='temperatura'
type='=', value='='
type='number', value='100'
type='.', value='.'
type='se', value='se'
type='observation', value='temperatura'
type='oplogic', value='>='
type='number', value='90'
type='entao', value='entao'
type='enviar', value='enviar'
type='alerta', value='alerta'
type='(', value='('
type='msg', value='"Muito caliente, está à "'
type=',', value=','
type='observation', value='temperatura'
type=')', value=')'
type='namedevice', value='Batata'
type='senao', value='senao'
type='action', value='desligar'
type='namedevice', value='Batata'
type='.', value='.'
""",

"""type='device', value='dispositivo'
type=':', value=':'
type='{', value='{'
type='namedevice', value='Batata'
type=',', value=','
type='observation', value='temperatura'
type='}', value='}'
type='set', value='set'
type='observation', value='temperatura'
type='=', value='='
type='number', value='100'
type='.', value='.'
type='se', value='se'
type='observation', value='temperatura'
type='oplogic', value='>='
type='number', value='90'
type='&', value='&'
type='&', value='&'
type='observation', value='temperatura'
type='oplogic', value='<'
type='number', value='1000'
type='entao', value='entao'
type='enviar', value='enviar'
type='alerta', value='alerta'
type='(', value='('
type='msg', value='"Muito caliente, está à "'
type=',', value=','
type='observation', value='temperatura'
type=')', value=')'
type='namedevice', value='Batata'
type='.', value='.'
"""
]

ans_Parser = [
"""[
{"DEVICE" : "Termometro"},
{"DEVICE_OBS" : "Batata, temperatura"}
]""",

"""[
{"DEVICE_OBS" : "Batata, temperatura"},
{"ATTRIB" : "temperatura, 1000"}
]""",

"""[
{"DEVICE" : "Batata"},
{"ligar" : "Batata"}
]""",

'''[
{"DEVICE" : "Batata"},
{"ALERT" : "\\\"Muito caliente\\\", Batata"}
]''',

"""[
{"DEVICE_OBS" : "Batata, temperatura"},
{"ATTRIB" : "temperatura, 100"},
{"ALERT_OBS" : "\\\"Muito caliente, está à \\\", temperatura, Batata"}
]""",

"""[
{"DEVICE" : "Batata"},
{"DEVICE" : "Cebola"},
{"ALERT_ALL" : "\\\"Sopa\\\", Batata, Cebola"}
]""",

"""[
{"DEVICE_OBS" : "Batata, temperatura"},
{"ATTRIB" : "temperatura, 100"},
{"IF" : "temperatura >= 90"},
{"ALERT_OBS" : "\\\"Muito caliente, está à \\\", temperatura, Batata"},
{"ENDIF" : ""}
]""",

"""[
{"DEVICE_OBS" : "Batata, temperatura"},
{"ATTRIB" : "temperatura, 100"},
{"IF" : "temperatura >= 90"},
{"ALERT_OBS" : "\\\"Muito caliente, está à \\\", temperatura, Batata"},
{"ELSE" : ""},
{"desligar" : "Batata"},
{"ENDIF" : ""}
]""",

"""[
{"DEVICE_OBS" : "Batata, temperatura"},
{"ATTRIB" : "temperatura, 100"},
{"IF" : "temperatura >= 90&&temperatura < 1000"},
{"ALERT_OBS" : "\\\"Muito caliente, está à \\\", temperatura, Batata"},
{"ENDIF" : ""}
]"""
]

def test_Lexer_dispositivos():
    test_tokenize = "dispositivo:{Termometro}\n dispositivo:{Batata, temperatura}"
    res = lexer.tokenize(test_tokenize)
    return res

def test_Parser_dispositivos():
    test_tokenize = "dispositivo:{Termometro}\n dispositivo:{Batata, temperatura}"
    res = parser.parse(lexer.tokenize(test_tokenize))
    return res

def test_Lexer_attrib():
    test_tokenize = "dispositivo:{Batata, temperatura}\n set temperatura = True."
    res = lexer.tokenize(test_tokenize)
    return res

def test_Parser_attrib():
    test_tokenize = "dispositivo:{Batata, temperatura}\n set temperatura = 1000."
    res = parser.parse(lexer.tokenize(test_tokenize))
    return res

def test_Lexer_act():
    test_tokenize = "dispositivo:{Batata}\n ligar Batata."
    res = lexer.tokenize(test_tokenize)
    return res

def test_Parser_act():
    test_tokenize = "dispositivo:{Batata}\n ligar Batata."
    res = parser.parse(lexer.tokenize(test_tokenize))
    return res

def test_Lexer_alert():
    test_tokenize = "dispositivo:{Batata}\n enviar alerta (\"Muito caliente\") Batata."
    res = lexer.tokenize(test_tokenize)
    return res

def test_Parser_alert():
    test_tokenize = "dispositivo:{Batata}\n enviar alerta (\"Muito caliente\") Batata."
    res = parser.parse(lexer.tokenize(test_tokenize))
    return res

def test_Lexer_alert_observation():
    test_tokenize = "dispositivo:{Batata, temperatura}\nset temperatura = 100.\nenviar alerta (\"Muito caliente, está à \", temperatura) Batata."
    res = lexer.tokenize(test_tokenize)
    return res

def test_Parser_alert_observation():
    test_tokenize = "dispositivo:{Batata, temperatura}\nset temperatura = 100.\nenviar alerta (\"Muito caliente, está à \", temperatura) Batata."
    res = parser.parse(lexer.tokenize(test_tokenize))
    return res

def test_Lexer_alert_all():
    test_tokenize = "dispositivo:{Batata}\ndispositivo:{Cebola}\n enviar alerta (\"Sopa\") para todos: Batata, Cebola."
    res = lexer.tokenize(test_tokenize)
    return res

def test_Parser_alert_all():
    test_tokenize = "dispositivo:{Batata}\ndispositivo:{Cebola}\n enviar alerta (\"Sopa\") para todos: Batata, Cebola."
    res = parser.parse(lexer.tokenize(test_tokenize))
    return res

def test_Lexer_obsact_if():
    test_tokenize = "dispositivo:{Batata, temperatura}\nset temperatura = 100.\nse temperatura >= 90 entao enviar alerta (\"Muito caliente, está à \", temperatura) Batata."
    res = lexer.tokenize(test_tokenize)
    return res

def test_Parser_obsact_if():
    test_tokenize = "dispositivo:{Batata, temperatura}\nset temperatura = 100.\nse temperatura >= 90 entao enviar alerta (\"Muito caliente, está à \", temperatura) Batata."
    res = parser.parse(lexer.tokenize(test_tokenize))
    return res

def test_Lexer_obsact_if_else():
    test_tokenize = "dispositivo:{Batata, temperatura}\nset temperatura = 100.\nse temperatura >= 90 entao enviar alerta (\"Muito caliente, está à \", temperatura) Batata senao desligar Batata."
    res = lexer.tokenize(test_tokenize)
    return res

def test_Parser_obsact_if_else():
    test_tokenize = "dispositivo:{Batata, temperatura}\nset temperatura = 100.\nse temperatura >= 90 entao enviar alerta (\"Muito caliente, está à \", temperatura) Batata senao desligar Batata."
    res = parser.parse(lexer.tokenize(test_tokenize))
    return res

def test_Lexer_obsact_observations():
    test_tokenize = "dispositivo:{Batata, temperatura}\nset temperatura = 100.\nse temperatura >= 90 && temperatura < 1000 entao enviar alerta (\"Muito caliente, está à \", temperatura) Batata."
    res = lexer.tokenize(test_tokenize)
    return res

def test_Parser_obsact_observations():
    test_tokenize = "dispositivo:{Batata, temperatura}\nset temperatura = 100.\nse temperatura >= 90 && temperatura < 1000 entao enviar alerta (\"Muito caliente, está à \", temperatura) Batata."
    res = parser.parse(lexer.tokenize(test_tokenize))
    return res

test_functions_Lexer = [
    test_Lexer_dispositivos,
    test_Lexer_attrib,
    test_Lexer_act,
    test_Lexer_alert,
    test_Lexer_alert_observation,
    test_Lexer_alert_all,
    test_Lexer_obsact_if,
    test_Lexer_obsact_if_else,
    test_Lexer_obsact_observations,
]

test_functions_Parser = [
    test_Parser_dispositivos,
    test_Parser_attrib,
    test_Parser_act,
    test_Parser_alert,
    test_Parser_alert_observation,
    test_Parser_alert_all,
    test_Parser_obsact_if,
    test_Parser_obsact_if_else,
    test_Parser_obsact_observations,
]

test_base_file_loc = './test_files/test_X.obsact'
test_file_expected_error = [
    False,
    True,
    True,
    True,
    False,
    True,
    False,
    False
]

if __name__ == '__main__':
    print("Testing Lexer:")
    for (i, test) in enumerate(test_functions_Lexer):
        res = test()
        s = ''
        for tok in res:
            s += 'type=%r, value=%r\n' % (tok.type, tok.value)
        if ans_Lexer[i] == s:
            print('Lexer Test #%d: OK' % i)
        else:
            print('lexer Test #%d: FAIL' % i)
            print(s)
            print(ans_Lexer[i])

    print()
    print("Testing Parser:")
    for (i, test) in enumerate(test_functions_Parser):
        res = test()
        if ans_Parser[i] == res:
            print('Parser Test #%d: OK' % i)
        else:
            print('parser Test #%d: FAIL' % i)
            print(res)
            print(ans_Parser[i])

    print()
    print("Testing obsact test files:")
    for (i, exp) in enumerate(test_file_expected_error):
        curr_filename = test_base_file_loc.replace('X', str(i + 1))
        with open(curr_filename, 'r') as f:
            try:
                res = parser.parse(lexer.tokenize(f.read()))
                print('No Syntax Error on file %s' % (curr_filename))
                if not exp:
                    print('No error expected, continuing.')
                else:
                    print('Error expected, stopping.')
                    break
            except Exception as e:
                print('Syntax Error on file %s: %s' % (curr_filename, e))
                if exp:
                    print('Error Expected, continuing.')
                else:
                    print('Error Not Expected, stopping.')
                    break

        print()
    print("Tests completed")