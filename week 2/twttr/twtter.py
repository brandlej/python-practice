def main():
    print("Output: ", remove_vowels(input("Input: ").strip()))

def remove_vowels(text: str):
    formatted_text = ""
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in text:
        if(char.lower() in vowels):
            continue
        formatted_text += char
    
    return formatted_text


main()