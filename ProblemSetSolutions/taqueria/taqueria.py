def main():
    get_price()

def get_price():
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        }
    subtotal = 0
    while True:
        try:
            userMenu = input("Item: ").title()
            if userMenu in menu:
                subtotal += menu[userMenu]
            print(f"Total: ${subtotal:.2f}")

        except EOFError:
            print()
            break

main()