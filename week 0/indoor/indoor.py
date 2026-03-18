def main():
    # get user input and print as is
    text = input()

    # output user input lowercase
    print(convertToIndoorVoice(text))


def convertToIndoorVoice(text: str):
    return text.lower()


main()
