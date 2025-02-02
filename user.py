import os
os.system('cls' if os.name == 'nt' else 'clear')

user_info = {
    "name": input("What is the user's name? "),
    "age": input("What is the user's age? "),
    "country_of_birth": input("What is the user's country of birth? "),
    "known_for": input("What is the user known for? ")
}

print("\nUser Information:", user_info)
