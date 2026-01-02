import time

def bit_converter():

    while True:
        print("\n ***** Bit Converter Menu *****")
        print("1. Character to ASCII")
        print("2. ASCII to Character")
        print("3. Decimal to Binary")
        print("4. Binary to Decimal")
        print("5. Octal to Decimal")
        print("6. Decimal to Octal")
        print("7. Hexadecimal to Decimal")
        print("8. Decimal to Hexadecimal")
        print("9. Exit")

        choice = input("Enter your choice (1-9):")
        if choice == "1":
            char = input("Enter a Character:")
            print(" ASCII value is: ",ord(char))
        
        elif choice == "2":
            num = int(input("Enter ASCII Value:"))
            print("Charater is ", chr(num))

        elif choice == "3":
            dec = int(input("Enter a Decimal Number:"))
            print("Binary is ",format(dec,"b"))

        elif choice == "4":
            bin = input("Enter a Binary Number:")
            print("Decimal is ",int(bin,2))
        
        elif choice == "5":
            octal = input("Enter a Octal Number:")
            print("Decimal is:",int(octal,8))
        
        elif choice == "6":
            dec = int(input("Enter a decimal Number:"))
            print("Octal  is: ",format(dec,"o"))

        elif choice  == "7":
            hexa = input("Enter a Hexadecimal Number:")
            print("Decimal is :",int(hexa,16))

        elif choice == "8":
            dec = int(input("Enter a Decimal Number :"))
            print("Hexadecimal is ",format(dec,"x"))

        elif choice == "9":
            print("...Exiting...")
            break

        else:
            print("Invalid choice. Try Again...")

        back = input("\n Do You Want To Go Back To Menu? (y/n):").lower()

        if back!="y":
            print("Okay! Exiting Bit Converter. See You Soon!!")
            break

bit_converter()