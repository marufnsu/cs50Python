def main():
    fraction = convert(input("Fraction: "))
    percentage = gauge(fraction)
    print(percentage)

def convert(fraction):

    while True:
        try:
            x, y = fraction.split("/")
            x, y = int(x), int(y)
            fraction = (x/y)
            if fraction <= 1:
                fraction = round(fraction * 100)
                return fraction
            else:
                fraction = input("Fraction: ")
                pass

        except (ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
    if percentage <= 1:
        return ("E")
    elif percentage >= 99:
        return ("F")
    else:
        return (f"{percentage}%")

if __name__ == "__main__":
    main()
