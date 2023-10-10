from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

if len(sys.argv) == 1:
    isRandom = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    isRandom = False
else:
    sys.exit("Invalid usage")

figlet.getFonts()
if isRandom == False:
    try:
        figlet.setFont(font=sys.argv[2])
    except:
        sys.exit("Invalid usage")
else:
    font = random.choice(figlet.getFonts())

usrInput = input("Input: ")
print("Output:")
print(figlet.renderText(usrInput))