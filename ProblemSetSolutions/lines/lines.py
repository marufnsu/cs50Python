import sys

def main():
    verify_cmd_arg()
    try:
        with open(sys.argv[1]) as file:
            lines = file.readlines()

    except FileNotFoundError:
        sys.exit("File does not exist")

    count = 0
    for line in lines:
        if count_line(line) == False:
            count += 1
    print(count)

def verify_cmd_arg():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")

def count_line(line):
    if line.isspace():
        return True
    elif line.lstrip().startswith("#"):
        return True
    else:
        return False

if __name__ == "__main__":
    main()