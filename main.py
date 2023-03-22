# Author: Jitesh Mandal
# Location: Delhi
# Date: 18-03-2023

from random import randint
from time import ctime
import json

# All Records
records = {}

# Import all data to records dict
with open("records.json", "r") as jsonFile:
    records.update(json.load(jsonFile))

# Function to give hint to user
def give_hint(r_num, u_num):
    if r_num > u_num:
        print(f"Number is greater than {u_num}!")
    elif r_num < u_num:
        print(f"Number is smaller than {u_num}!")
    else:
        print("Congrats, You WON!!!")


# Function to write score in "scores.txt" file
def write_record(name, attempt, level):
    if name in records.keys():
        print("Name already exist!")
        records[name].append([f"{ctime()}", attempt, level])
    else:
        print("Name don't exist!")
        records.update({name: [[f"{ctime()}", attempt, level]]})
    with open("records.json", "w") as recordsFile:
        recordsFile.write(json.dumps(records, indent=5))



# Get All The Records
def get_records():
    name = input("\nEnter Your Name: ").lower()

    if name in records:
        print("\n\nSno.\tDate Played\t\t\tAttempts\tLevel\n")
        info = records[name]
        for i, lst in enumerate(info, start=1):
            date, attempts, level = lst
            print(f"{i}.\t{date}\t{attempts}\t\t{level}")
        print("\n\n")
    else:
        print(f"Data not available for {name}")




while True:
    options = input('''Welcome to GUESS THE NUMBER!!!!
    1. Start Game
    2. Check Your Records (Update: Fixed)
    3. Exit

    Choose Your Option: ''')

    match options:
        case "1":
            name = input("Enter your name to continue: ").lower()
            level = input("\n\nSelect Your Level\n     1. Easy\n     2. Medium\n     3. Hard\n\n     Please input your selection: ")
            lvl = {
                "easy": 20,
                "medium": 40,
                "hard": 100
            }

            match level:
                case "1":
                    level = "easy"
                    number = randint(0, 20)
                case "2":
                    level = "medium"
                    number = randint(0, 40)
                case "3":
                    level = "hard"
                    number = randint(0, 100)
                case _:
                    print("Invalid Selection!")

            if level in lvl.keys():
                attempt = 0
                while True:
                    guess = input(f"\n\nEnter Your Guess Between 0 and {lvl[level]}: ")

                    while type(guess) != int:
                        try:
                            guess = int(guess)
                        except ValueError:
                            print("Please enter an integer only!")
                            guess = input(f"Enter Again (0 - {lvl[level]}): ")
                    
                    give_hint(number, guess)
                    attempt += 1

                    if guess == number:
                        print(f"You guessed the number in {attempt} attemps!")
                        write_record(name, attempt, level)
                        break

        case "2":
            get_records()
        case "3":
            print("User Typed Exit!\n Exiting!")
            exit()
        case _:
            print("Invalid Selection!")
