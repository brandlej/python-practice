def main():
    text = input()
    print(convertFaces(text))

def convertFaces(text: str):
    return text.replace(":)", "🙂").replace(":(", "🙁")

main()