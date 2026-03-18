def main():
    hello("world")
    goodbye("world")


def hello(name: str):
    print(f"hello, {name}")


def goodbye(name: str):
    print(f"goodbye, {name}")


# __name__ is a special built-in variable in Python
# It is set to "__main__" when this file is run directly
# It is set to the module name when imported
# This allows the file to be both runnable and importable
if __name__ == "__main__":
    main()
