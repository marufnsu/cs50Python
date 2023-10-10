import emoji

userInput = input("Input: ")
emojiConvert = emoji.emojize(userInput, language = 'alias')
print(f"Output: {emojiConvert}")