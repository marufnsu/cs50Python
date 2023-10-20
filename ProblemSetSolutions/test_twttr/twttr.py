def main():
    word = input("Input: ").strip()
    print(f"Output: {shorten(word)}")

def shorten(word):
    vowels = ['a','e','i','o','u']
    for chr in word:
        if chr.lower() in vowels:
            word = word.replace(chr, "")
        else:
            continue
    return word

if __name__ == "__main__":
    main()