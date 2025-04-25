name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

print("I", name, "am", age, "years old, and I'm", height, "meters tall.")

if age >= 50:
    print("Ik ben kapot oud")
elif age >= 18:
    print("Ik ben volwassen")
else:
    print("Ik ben een kind")

if height >= 1.80:
    print("Valid lengte")
else:
    print("Invalid lengte")