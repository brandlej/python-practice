import sys
import random
import argparse
from pyfiglet import Figlet
from typing import NoReturn


# override argparser error method using a child class of
# ArgumentParser
class CustomArgumentParser(argparse.ArgumentParser):
    # override error so we can exit with "invalid usage" for the program
    # which is what solution requires
    def error(self, message: str) -> NoReturn:
        sys.exit("Invalid usage")


def main():
    # init arg parser using child class
    # this will allow us to exit with custom error method
    # if invalid option provided
    parser = CustomArgumentParser()
    # register flag
    parser.add_argument("-f", "--font")
    # parse args
    args = parser.parse_args()

    if args.font:
        text = input("Input: ")
        print_figlet_text(text, args.font)
    else:
        text = input("Input: ")
        print_figlet_text(text, None)


def print_figlet_text(
    text: str,
    font: str | None,
):
    figlet = Figlet()
    fonts = figlet.getFonts()

    if font:
        if font not in fonts:
            sys.exit("Invalid usage")

        figlet.setFont(font=font)
        print(figlet.renderText(text))
    else:
        figlet.setFont(font=random.choice(fonts))
        print(figlet.renderText(text))


if __name__ == "__main__":
    main()
