import json
from lua import lua_dict
from java import java_dict
from c import c_dict

langs = {
    'lua' : lua_dict,
    'java' : java_dict,
    'c': c_dict
}

def translate(out_name: str, tokens: list, table: dict) -> None:
    with open(out_name, "w") as out_file:
        out_file.write(table['PRECODE']())
        for token in tokens:
            for key, value in token.items():
                args = [v.strip() for v in value.split(', ')]
                out_file.write(table[key](args))
        out_file.write(table['AFTERCODE']())
    return

if __name__ == '__main__':
    test = json.loads('[{"DEVICE_OBS" : "Batata, temperatura"},{"DEVICE" : "Cebola"},{"ATTRIB" : "temperatura, 100"}]')
    translate('output.lua', test, lua_dict)