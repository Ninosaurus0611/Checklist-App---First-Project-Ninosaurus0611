name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
sex = input("Enter your gender, Male or Female: ")

print("I", name, "am", sex, age, "years old, and I'm", height, "meters tall.")

#General info
#Age
if age >= 50:
    print("Ik ben kapot oud")
elif age >= 18:
    print("Ik ben volwassen")
else:
    print("Ik ben een kind")

#Male
if sex == "Male":
#Length
    if height >= 1.80:
        print("Valid lengte")
    else:
        print("Invalid lengte")

#Female
if sex == "Female":
#Length
    if height >= 1.73:
        print("Damn, basketball looking ahh")
    elif 1.65 < height < 1.73:
        print("Goddess")
    elif 1.57 < height < 1.65:
        print("Queen")
    else:
        print("Angel")
