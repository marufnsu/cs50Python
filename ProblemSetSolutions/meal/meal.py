def main():
    user_input = input("Enter the time in 24 hours format: ").strip()
    return convert(user_input)

def convert(time):
    hr , sec = time.split(":")
    timeInDecimal = float(hr) + float(sec)/60
    timeInDecimal = round(timeInDecimal,2)

    if 7<= timeInDecimal <=8:
        print("breakfast time")
    elif 12<= timeInDecimal <=13:
        print("lunch time")
    elif 18<= timeInDecimal <=19:
        print("dinner time")

    return timeInDecimal


if __name__ == "__main__":
    main()