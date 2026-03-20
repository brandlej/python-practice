def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def hello(to: str = "world"):
    return f"hello, {to}"


def get_int(prompt: str):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            # print("x is not an integer")
            pass


if __name__ == "__main__":
    main()

# SyntaxError - error with syntax
# ValueError - error with a given value
# NameError - error with name of variable not existing in scope
