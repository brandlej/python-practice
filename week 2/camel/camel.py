def main():
    text = input("camelCase: ")

    print("snake_case: ", convert_camel_to_snake(text))

def convert_camel_to_snake(text: str):
    formatted = text.strip()
    snake_text = ""

    for char in formatted:
        if(char.isupper()):
            snake_text += "_" + char
        else:
            snake_text += char
    return snake_text.lower()

main()