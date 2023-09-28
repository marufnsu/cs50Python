def main():
    #user input for replacement
    usrStr = input("What is the sentence to convert? ")
    print(convert(usrStr))

def convert(sentence):
    #replace emoticon with emojis
    sentence = sentence.replace(":)", "🙂")
    sentence = sentence.replace(":(", "🙁")

    return sentence

main()