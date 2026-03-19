import sys
import random
from pyfiglet import Figlet


# checks are kind of brittle
# would be more idiomatic to use std library argparse from python
def main():
    # no cli args - output text in random font
    if len(sys.argv) == 1:
        text = input("Input: ")

        print_figlet_text(text, None)
    # 2 cli args - output text in given font
    elif len(sys.argv) == 3:
        option, font = sys.argv[1:]

        # validate valid font option
        if option != "-f" and option != "--font":
            sys.exit("Invalid usage")

        text = input("Input: ")
        print_figlet_text(text, font)
    else:
        sys.exit("Invalid usage")


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
