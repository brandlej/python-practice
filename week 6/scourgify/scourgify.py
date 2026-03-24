import csv
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    source_csv = sys.argv[1]
    target_csv = sys.argv[2]

    # python allows opening both files in one line with comma
    # use streaming approach to write as i'm reading the source csv
    try:
        with open(source_csv) as source, open(target_csv, "w") as target:
            reader = csv.DictReader(source)
            writer = csv.DictWriter(target, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in reader:
                last, first = row["name"].split(", ")
                writer.writerow({"first": first, "last": last, "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {source_csv}")


if __name__ == "__main__":
    main()
