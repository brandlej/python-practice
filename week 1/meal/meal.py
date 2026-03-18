def main():
    time = input("What time is it? ")
    timeDec = convert(time)

    if timeDec >= 7 and timeDec <= 8:
        print("breakfast time")
    elif timeDec >= 12 and timeDec <= 13:
        print("lunch time")
    elif timeDec >= 18 and timeDec <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    minutesDec = float(minutes) / 60

    return round(float(hours) + minutesDec, 1)

if __name__ == "__main__":
    main()