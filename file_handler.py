import json
import os


def load_birthdays():
    if os.path.exists("birthdays.json"):
        with open("birthdays.json", "r") as file:
            return json.load(file)


    return []


def save_birthdays(birthdays):
    with open("birthdays.json", "w") as file:
        json.dump(birthdays, file, indent=4)