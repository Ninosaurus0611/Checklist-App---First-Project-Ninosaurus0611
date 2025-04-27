#Welcome
print("Hello!\nWelcome to your first test.\n")

#1st question
start_survey = input("Do you wish to proceed? \nYes or No?\n")
if start_survey == "Yes" or start_survey == "yes":
    print("\nYou are now ready to proceed.\n")
elif start_survey == "No" or start_survey == "no":
    print("\nCome back any time")
    exit()

#1st introduction
name = input("What is your name?\n")
print(f"\n{name}, that's a nice name!\n")

#start questions
age = int(input(f"How old are you {name}?\n"))

#funny
sex = input("\nAre you a Male or Female\n")
if sex == "Male" or sex == "male":
    print("\nNice, sup dude")
elif sex == "Female" or sex == "female":
    print("\na dame, how wonderfull of you to join me this evening.")
while sex not in ("Male", "male", "Female", "female"):
    print("\nInvalide input")
    sex = input("\nAre you a Male or Female\n")

hair_color = input("\nWhat is your hair color?\n")

height = float(input(f"\nHow tall are you {name}?\n"))

print("So if i've correctly understood you, you are:", name, sex, "age", age, "your hair is", hair_color,"and you are", height, "meters tall.")
statement = input("\nIs that right?\n")
if statement == "Yes" or statement == "yes":
    print("\nPerfect!\n")
elif statement == "No" or statement == "no":
    print("\nOh well, it didn't matter anyways.")
while statement not in ("Yes", "yes", "No", "no"):
    print("\nI don't copy, did I understand you correctly?")

#General info
#Age
if age >= 50:
    print("Kapot oud")
elif age >= 18:
    print("Volwassen")
else:
    print("Je bent een kind")

#miss weg of integreren?
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
