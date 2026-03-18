def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt: str):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            # print("x is not an integer")
            pass

main()

# SyntaxError - error with syntax
# ValueError - error with a given value
# NameError - error with name of variable not existing in scope