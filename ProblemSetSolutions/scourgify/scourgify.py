import sys
import csv
from tabulate import tabulate

def main():
    verify_cmd_arg()
    name_output = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                name_split = row["name"].split(",")
                name_output.append({'first':name_split[1].lstrip(), 'last':name_split[0], 'house': row['house']})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
        writer.writerow({"first" : "first", "last" : "last", "house" : "house"})
        for row in name_output:
            writer.writerow({"first" : row["first"], "last" : row["last"], "house" : row["house"]})

def verify_cmd_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()