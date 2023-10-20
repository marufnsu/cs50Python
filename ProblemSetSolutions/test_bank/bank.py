def main():
    greetings = input("Greet someone with greetings: ")
    print(f"${value(greetings)}")


def value(greeting):
    greeting = greeting.lstrip().lower()

    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()