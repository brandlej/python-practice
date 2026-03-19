import inflect


def main():
    p = inflect.engine()
    names: list[str] = []
    while True:
        try:
            names.append(input("Name: "))
        except EOFError:
            break

    print("Adieu, adieu, to", p.join(names))  # type: ignore


if __name__ == "__main__":
    main()
