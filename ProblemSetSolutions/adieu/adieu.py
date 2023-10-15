import inflect
def main():
    inflector = inflect.engine()
    grocery = get_list()
    updatedList = inflector.join(grocery)
    print(f"Adieu, adieu, to {updatedList}")

def get_list():
    nameList = []

    while True:
        try:
            userItem = input("Name: ")
            nameList.append(userItem)
        except EOFError:
            return nameList

main()