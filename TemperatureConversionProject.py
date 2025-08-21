# Temperature conversion project Celsius, Fahrenheit and Kelvin

measurement = input("Enter celsius, Kelvin Fahrenheit (C/K/F): ")
temp = int(input("Enter temperature: "))

if measurement == "K":
    temp = temp - 273.15
    print(f"{round(temp, 2)}C")
if measurement == "F":
    temp = (temp - 32) * 5 / 9 + 273.15
    print(f"{round(temp, 2)}K")
elif measurement == "C":
    temp = (temp * 9) / 5 + 32
    print(f"{round(temp, 2)}F")
elif measurement == "F":
    temp = (temp - 32) * 5 / 9
    print(f"{round(temp, 2)}C")
else:
    print(f"({measurement} is not a valid in put)")
