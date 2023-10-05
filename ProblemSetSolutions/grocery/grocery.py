def main():
    grocery = get_list()
    for key in sorted(grocery.keys()):
        print(f"{grocery[key]} {key}")
        
def get_list():
    groceryList = {}

    while True:
        try:
            userItem = input().upper()
            if userItem in groceryList:
                groceryList[userItem] += 1
            else:
                groceryList[userItem] = 1

        except EOFError:
            return groceryList

main()