import sys
import json

from translator import translate, langs
from analyzer import analyze

def main(file_name: str, language: str) -> None:
    tokens = []
    try:
        lang_dict = langs[language.lower()]
    except KeyError:
        print("Please select a valid language (lua, java...)")
        return
    output_filename = "output." + language
    if file_name.endswith('.obsact'):
        try:
            tokens = analyze(file_name)
            translate(output_filename, json.loads(tokens), lang_dict)
        except Exception as e:
            print("Syntax error", e)
            return
    else:
        print("File must be of type .obsact")
    return


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '-l' or sys.argv[1] == '--list':
            print("Available languages:\n\t- Lua\n\t- Java\n\t- C")
        elif not len(sys.argv) == 3:
            print("Usage: python3 main.py <file_name> <language>\nUsage: python3 main.py --list (or -l)")
        else:
            main(sys.argv[1], sys.argv[2])
