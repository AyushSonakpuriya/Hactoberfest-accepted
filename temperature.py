choice = input("Convert from (C/F): ").upper()
temp = float(input("Enter temperature: "))

if choice == 'C':
    print("Temperature in Fahrenheit:", (temp * 9/5) + 32)
elif choice == 'F':
    print("Temperature in Celsius:", (temp - 32) * 5/9)
else:
    print("Invalid choice")
