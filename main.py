import sys

from translator import translate
from analyzer import analyze

def main(file_name: str) -> None:
    tokens = []
    if file_name.endswith('.obsact'):
        tokens = analyze(file_name)
        if len(tokens) != 0:
            for error in tokens:
                print(error)
            return
    else:
        print("File must be of type .obsact")

    translate(tokens)
    return


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <file_name>")
    else:
        main(sys.argv[1])
