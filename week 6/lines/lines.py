import sys
from typing import TextIO


def main():
    # check valid args length
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # check it's a python file
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a python file")

    # try to open file
    try:
        with open(sys.argv[1]) as file:
            print(count_lines_of_code(file))
    except FileNotFoundError:
        sys.exit("File does not exist")


def count_lines_of_code(file: TextIO):
    count = 0
    for line in file:
        parsed_line = line.strip()
        if parsed_line == "" or parsed_line.startswith("#"):
            continue
        count += 1
    return count


if __name__ == "__main__":
    main()
