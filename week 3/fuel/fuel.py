def main():
    # This structure separates logic from I/O and allows
    # us to unit test helper functions
    while True:
        try:
            percent = convert(input("Fraction: "))
            print(gauge(percent))
            break
        except (
            ValueError,
            ZeroDivisionError,
        ):
            continue


def gauge(percent: int):
    if percent <= 1:
        return "E"
    elif percent >= 99:
        return "F"
    else:
        return f"{percent}%"


def convert(fraction: str):
    num, denom = fraction.split("/")
    # python will raise naturally here which is what we want
    # more pythonic
    x = int(num)
    y = int(denom)

    # if y is zero raise a zero div error
    if y == 0:
        raise ZeroDivisionError

    # if x > y raise a value error
    if x > y:
        raise ValueError

    return round((x / y) * 100)


if __name__ == "__main__":
    main()
