import emoji


def main():
    name = input("Input: ").strip().lower()

    print(emoji.emojize(name, language="alias"))


if __name__ == "__main__":
    main()
