speedOfLightMps = 300000000

def main():
    # capture user input and convert to int (assume)
    mass = int(input("m: "))
    
    # calulate energy using int and print
    print(calculateEnergy(mass))

def calculateEnergy(mass: int):
    return mass * (speedOfLightMps ** 2)

main()