while True:
    menu = input("1-Enter temperature as celsius\n2-Enter temperature as fahrenheit\n3-Enter temperature as kelvin\n4-Exit\n")
    if menu == "1":
        celsius = float(input("Please enter temperature: "))
        print(f"Celcius: {celsius} - Fahrenheit: {celsius * 9 / 5 + 32} - Kelvin: {celsius + 273.15}")
    elif menu == "2":
        fahrenheit = float(input("Please enter temperature: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"Celcius: {celsius} - Fahrenheit: {fahrenheit} - Kelvin: {celsius + 273.15}")
    elif menu == "3":
        kelvin = float(input("Please enter temperature: "))
        celsius = kelvin - 273.15
        print(f"Celcius: {celsius} - Fahrenheit: {celsius * 9 / 5 + 32} - Kelvin: {kelvin}")
    elif menu == "4":
        print("Quitting...")
        break
    else:
        print("Please enter a valid number")
