def main():
    accepted_denominations = [25, 10, 5]

    cost = 50
    total = 0
    while (total < cost):
        print("Amount Due: ", cost - total)
        coin = int(input("Insert Coin: ").strip())

        if coin not in accepted_denominations:
            print()
            continue

        total += coin
        print()

    print("Change owed: ", total - cost)

main()