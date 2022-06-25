from sys import argv
from src.driver import startApp

def main():

    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()
    results = startApp(Lines)
    for result in results:
        print(*result)

if __name__ == "__main__":
    main()
