import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    verify_cmd_arg()

    try:
        imgFile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirtImg = Image.open("shirt.png")
    size = shirtImg.size
    muppet = ImageOps.fit(imgFile, size)
    muppet.paste(shirtImg, shirtImg)
    muppet.save(sys.argv[2])

def verify_cmd_arg():
    img1 = splitext(sys.argv[1])
    img2 = splitext(sys.argv[2])
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif check_img_ext(img1[1]) == False:
        sys.exit("Invalid input")
    elif check_img_ext(img2[1]) == False:
        sys.exit("Invalid output")
    elif img1[1].lower() != img2[1].lower():
        sys.exit("Input and output have different extensions")

def check_img_ext(img):
    if img in [".jpg", ".jpeg", ".png"]:
        return True
    return False

if __name__ == "__main__":
    main()
