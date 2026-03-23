def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def has_illegal_char(s: str):
    illegal_chars = [".", " ", "'", '"']
    for char in s:
        if char in illegal_chars:
            return True
    return False


def has_illegal_numbers(s: str):
    for i, char in enumerate(s):
        if char.isdigit():
            if char == "0":
                return True

            # everything after must be digits
            if not s[i:].isdigit():
                return True

            # once we enter this if block, we can break at the end since
            # we have already checked everything else
            break
    return False


def is_valid(s: str):
    # min 2 characters and max 6 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # start with 2 letters
    if not s[:2].isalpha():
        return False

    # numbers must come at end of plate, not middle
    # first number can't be zero
    if has_illegal_numbers(s):
        return False

    # no periods, spaces, or punctuation marks allowed
    if has_illegal_char(s):
        return False

    return True


if __name__ == "__main__":
    main()
