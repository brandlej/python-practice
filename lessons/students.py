import csv


def main():
    name = input("What's your name? ")
    home = input("Where's your home? ")

    with open("students.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "home"])
        writer.writerow({"name": name, "home": home})


if __name__ == "__main__":
    main()
