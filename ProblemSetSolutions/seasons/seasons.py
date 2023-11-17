from datetime import date
import re, sys, inflect

p = inflect.engine()

def main():
    birthday = input("Date of Birth: ")
    try:
        year, month, day = check_birthday(birthday)
    except:
        sys.exit("Invalid Date")
    date_of_birth = date(year, month, day)
    date_of_today = date.today()
    diff_in_days = (date_of_today - date_of_birth).days
    days_in_min = diff_in_days * 24 * 60
    words = p.number_to_words(days_in_min, andword = "")
    print(f"{words.capitalize()} minutes")

def check_birthday(birthday):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birthday):
        year, month, day = birthday.split("-")
        return int(year), int(month), int(day)


if __name__ == "__main__":
    main()
