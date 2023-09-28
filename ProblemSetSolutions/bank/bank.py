greetings = input("Greet someone with greetings: ")
greetings = greetings.lstrip().lower()

if greetings.startswith("hello"):
    print("$0")
elif greetings.startswith("h"):
    print("$20")
else:
    print("$100")