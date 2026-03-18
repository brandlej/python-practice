import random

# count = {"heads": 0, "tails": 0}

# i = 0
# while i < 1000000:
#     decision = random.choice(["heads", "tails"])
#     count[decision] = count.get(decision, 0) + 1
#     i += 1

# for side in count:
#     print(f"{side}: ", count[side])

# number = random.randint(1, 10)
# print(number)

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
