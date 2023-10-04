def main():
    fuel = get_fuel()
    if fuel <= 1:
        print("E")
    elif fuel >= 99:
        print("F")
    else:
        print(f"{fuel}%")

def get_fuel():
    while True:
        fuel = input("Fraction: ")
        try:
            x, y = fuel.split("/")
            x, y = int(x), int(y)
            percen = (x/y)
            if percen <= 1:
                break

        except (ValueError, ZeroDivisionError):
            pass

    Percen = round(percen * 100)
    return Percen

main()
