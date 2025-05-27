import sys
import pathlib

def main(filename):
    path = pathlib.Path(filename)
    with open(path) as f:
        contents = f.read()
        print(contents)

if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)