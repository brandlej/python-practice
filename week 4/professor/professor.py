import random
from typing import TypedDict


# custom type for problem dict
# so we can do list[Problem] for type hint
class Problem(TypedDict):
    question: str
    answer: str


def main():
    level = get_level()
    problems = generate_problems(level)
    score = 0

    for problem in problems:
        count = 0
        while True:
            # if max attempt, print answer and break out of loop
            if count == 3:
                print(f"{problem["question"]}{problem['answer']}")
                break

            print(problem["question"], end="")
            attempt = input()

            # if correct, break out of loop
            if attempt == problem["answer"]:
                score += 1
                break
            # keep looping for another attempt until limit
            else:
                print("EEE")
                count += 1
                continue

    print(f"Score: {score}")


def generate_problems(level: int):
    problems: list[Problem] = []
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        problems.append({"question": f"{x} + {y} = ", "answer": f"{x + y}"})

    return problems


def generate_integer(level: int) -> int:
    if level not in [1, 2, 3]:
        raise ValueError

    if level == 1:
        return random.randrange(0, 10)
    elif level == 2:
        return random.randrange(10, 100)
    else:
        return random.randrange(100, 1000)


def get_level() -> int:
    while True:
        try:
            n = int(input("Level: "))
            if n not in [1, 2, 3]:
                raise ValueError
            return n
        except ValueError:
            continue


if __name__ == "__main__":
    main()
