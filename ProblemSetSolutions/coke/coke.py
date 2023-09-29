coins_accepted = [5, 10, 25]
amount_due = 50

while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    coin_inserted = int(input("Enter a coin: "))
    if coin_inserted in coins_accepted:
        amount_due -= coin_inserted
    change_owed = abs(amount_due)
    print(f"Change Owed: {change_owed}")