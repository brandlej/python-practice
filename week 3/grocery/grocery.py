def main():
    # keep counts of each item
    groceries: dict[str, int] = {}

    # keep prompting
    while True:
        # pythonic, prompt and catch exception on just this bit
        try:
            # prompt user, case insensitive
            item = input().lower().strip()
        except EOFError:
            break

        # pythonic, check if in groceries
        # if item in groceries:
        #     groceries[item] += 1
        # else: #else set to 1
        #     groceries[item] = 1
        groceries[item] = groceries.get(item, 0) + 1

    # sort dict keys
    for item in sorted(groceries):
        # print count then item
        print(f"{groceries[item]} {item.upper()}")

main()