def main():
    words = input()
    intersperseEllipses(words)
    
def intersperseEllipses(words: str):
    print("...".join(words.split(" ")))

main()