def main():
    print(get_parsed_user_date())


MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def get_parsed_user_date():
    while True:
        date = input("Date: ").strip().title()

        normalizedIsoDate = parse_numeric_date(date) or parse_named_date(date)
        if normalizedIsoDate is not None:
            return normalizedIsoDate


def parse_numeric_date(date: str) -> str | None:
    try:
        month, day, year = date.split("/")
        month = int(month)
        day = int(day)

        if 1 <= month <= 12 and 1 <= day <= 31:
            return f"{year}-{month:02}-{day:02}"
    except ValueError:
        pass

    return None


def parse_named_date(date: str) -> str | None:
    try:
        month_day, year = date.split(", ")
        month, day = month_day.split(" ")
        month = MONTHS.index(month) + 1
        day = int(day)

        if 1 <= day <= 31:
            return f"{year}-{month:02}-{day:02}"
    except ValueError:
        pass

    return None


main()
