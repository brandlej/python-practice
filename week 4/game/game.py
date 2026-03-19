import random


def main():
    level = prompt_valid_number("Level: ")
    x = random.randint(1, level)

    while True:
        guess = prompt_valid_number("Guess: ")
        if guess < x:
            print("Too small!")
        elif guess > x:
            print("Too large!")
        else:
            print("Just right!")
            break


def prompt_valid_number(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value < 1:
                raise ValueError
            return value
        except ValueError:
            continue


if __name__ == "__main__":
    main()
