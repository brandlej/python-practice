def main():
    print(get_normalized_date())


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


def get_normalized_date():
    # loop until a valid normalized date to ISO
    while True:
        date = input("Date: ").strip().title()

        # check date against numeric parser
        normalized = parse_numeric_date(date)
        if normalized is not None:
            return normalized

        # check date against named parser
        normalized = parse_named_date(date)
        if normalized is not None:
            return normalized


# attempts to parse a numeric date
# if value error is thrown, pass and have fn return None
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


# attempts to parse a named date
# if value error is thrown, pass and have fn return None
def parse_named_date(date: str) -> str | None:
    # month dd, yyyy
    try:
        month_day, year = date.split(", ")
        month_str, day = month_day.split()  # splits out extra whitespace

        # check for month literal in list of months
        if month_str not in MONTHS:
            return None

        # get index of month against list position
        # works because static list is sorted
        # used in returned string literal
        month = MONTHS.index(month_str) + 1
        day = int(day)

        # don't need to check month here since we did above
        if 1 <= day <= 31:
            return f"{year}-{month:02}-{day:02}"
    except ValueError:
        pass

    return None


main()
