import csv
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    source_csv = sys.argv[1]
    target_csv = sys.argv[2]
    source_data: list[dict[str, str]] = []

    # could improve by writing to target dict as i'm reading

    # read csv rows into dict
    try:
        with open(source_csv) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row["name"].split(", ")
                source_data.append(
                    {"first": first, "last": last, "house": row["house"]}
                )
    except FileNotFoundError:
        sys.exit(f"Could not read {source_csv}")

    # write csv rows into dict
    # with updated csv header first, last, house
    with open(target_csv, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for entry in source_data:
            writer.writerow(entry)


if __name__ == "__main__":
    main()
