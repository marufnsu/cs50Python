vowels = ['a','e','i','o','u']
userInput = input("Please Enter your Input: ").strip()
for chr in userInput:
    if chr.lower() in vowels:
        userInput = userInput.replace(chr, "")
    else:
        continue
print(f"Output: {userInput}")