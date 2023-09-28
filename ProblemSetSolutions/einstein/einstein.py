def main():
    #user input for replacement
    usrStr = int(input("What is the mass in KGs? "))
    energy = einstein(usrStr)
    print(f"{energy:,}")

def einstein(mass):
    #Calculate the energy
    c = 300000000
    E = mass * (pow(c,2))

    return E

main()