userInput = input("CamelCase: ")
snake_case = ""
for c in userInput:
    if c == c.upper():
        c = "_" + c.lower()
        snake_case += c
    else:
        snake_case += c
print(f"snake_case:{snake_case}")