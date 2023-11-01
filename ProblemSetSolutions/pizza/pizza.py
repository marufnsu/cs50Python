import sys
import csv
from tabulate import tabulate

def main():
    verify_cmd_arg()
    store_table = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                store_table.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(store_table[1:], headers = store_table[0], tablefmt = "grid"))

def verify_cmd_arg():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()