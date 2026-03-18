def main():
    percent = get_percent()
    print_gauge_status(percent)

def print_gauge_status(percent: int):
    if percent <= 1:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"{percent}%")

def compute_percent(x: int, y: int):
    return round((x / y) * 100)

def get_percent():
    while True:
        try:
            fraction = input("Fraction: ")
            num, denom = fraction.split("/")
            # More pythonic to let attempt and let python throw and catch below
            # rather than pre-validate
            x = int(num)
            y = int(denom)

            if x > y:
                continue
            
            return compute_percent(x, y)
        except (ValueError, ZeroDivisionError): # more pythonic to catch zero division here
            continue

main()