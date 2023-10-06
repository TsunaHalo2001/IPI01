_ARG = 0.0029
_COP = 0.00023
_MXN = 0.055 

def convert(conversion):
    value = float(input("Enter the quantity "))
    USD = round(value*conversion,2)
    return USD

def main():
    print("Welcome to the money converter")
    print(" ")
    
    while (True):
        print("Select your currency")
        print("1. ARG")
        print("2. COP")
        print("3. MXN")
        print("4. Close")
        

        option = int(input())

        if(option == 1):
            USD = convert(_ARG)
        elif(option == 2):
            USD = convert(_COP)
        elif(option == 3):
            USD = convert(_MXN)
        elif(option == 4):
            return
        else:
            print("Invalid option")

        if(option >= 1 and option <=3):
            print(" ")
            print("The converted value is ",USD," USD")
            print(" ")
        


if __name__ == "__main__":
    main()