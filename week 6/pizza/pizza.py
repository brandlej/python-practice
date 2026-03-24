import csv
import sys
from tabulate import tabulate


def main():
    # guard against correct # args
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    # guard against invalid file type
    if not sys.argv[1].lower().endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        table = tabulate(
            get_menu_table(sys.argv[1]),  # takes the list of dicts built
            headers="keys",  # headers are keys of dicts
            tablefmt="grid",  # format specifier
        )
    except FileNotFoundError:
        sys.exit("File does not exist")

    # keep outside of try/except above for cleaner exception scope since print
    # won't raise that error
    print(table)


def get_menu_table(file_name: str) -> list[dict[str, str]]:
    # open and get file handle
    with open(file_name) as file:
        # list of dicts (where key is str, val is string)
        menu: list[dict[str, str]] = []
        # init a dictreader
        reader = csv.DictReader(file)

        # iterate over every row of data
        for row in reader:
            # append to list of dicts
            menu.append(row)

    return menu


if __name__ == "__main__":
    main()
