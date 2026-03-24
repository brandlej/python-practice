# name = input("What's your name? ")

# # open returns a file handle to open file subsequently
# file = open("names.txt", "a")
# file.write(f"{name}\n")

# # close file
# file.close()

# below is more pythonic
# this will automatically handle file open/close
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

names: list[str] = []

with open("names.txt") as file:
    for line in file:
        # add each of students name to list
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}")
