def main():
    greeting = input("Greeting: ").strip().lower()
    print(f"Greeting: ${value(greeting)}")


def value(greeting: str) -> int:
    lowercase_greeting = greeting.lower()
    if lowercase_greeting.startswith("hello"):
        return 0
    elif lowercase_greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
