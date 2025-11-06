def convert():
    value = float(input("Enter value: "))
    choice = input("Type 'C2F' for Celsius to Fahrenheit or 'M2F' for Meters to Feet: ")

    if choice == "C2F":
        print((value * 9/5) + 32, "ºF")
    elif choice == "M2F":
        print((value * 9/5) + 32, "Feet")
    else 
    print("Wrong choice!") 

convert()   


