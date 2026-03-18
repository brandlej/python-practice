def main():
    print_square(3)

# def print_square(size: int):
#     # outer loop - for reach row
#     for i in range(size):
#         # inner loop - for each column in row
#         for j in range(size):
#             print('#', end="")
#         print()

def print_square(size: int):
    for _ in range(size):
        print("#" * size)

main()