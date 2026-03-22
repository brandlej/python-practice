def main():
    word = input("Input: ")
    print("Output: ", shorten(word))


def shorten(word: str):
    shortened_word = ""

    for char in word:
        if char.lower() in ["a", "e", "i", "o", "u"]:
            continue
        shortened_word += char

    return shortened_word


if __name__ == "__main__":
    main()
