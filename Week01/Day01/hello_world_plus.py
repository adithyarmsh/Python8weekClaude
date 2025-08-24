# this is my project for Day 1 in Python

print("*" * 33 )
print() #empty row
print("===Welcome to the Hello World Plus program!===")
print() #empty row
print("*" * 33 )
print()
name = input("What is your name? ")
age = input("What is your current age? ")
FavColor = input("What is your favorite color? ")

if name == "":
    name = "Friendly User"
if age == "":
    age = "**unknown**"
if FavColor == "":
    FavColor = "**notSure**"

print() #empty row
print(f"Hello {name}!! Welcome!  You are {age} years old! with a favorite color of {FavColor}!")
print() #empty row
print("*" * 33 )

    

