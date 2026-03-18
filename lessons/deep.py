def main():
    x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

    match x:
        case "42":
            print("Yes")
        case "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")

    # could also use a membership operator with an answers array
    # e.g. answers = [42, "forty-two", "forty two"]
    # expression if x in answers

main() 