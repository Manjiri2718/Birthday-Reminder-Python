def add_birthday(birthday_list, name, day, month, year):
    birthday = {
        "name": name,
        "day": day,
        "month": month,
        "year": year
    }
    birthday_list.append(birthday)

def view_birthdays(birthday_list):
    if not birthday_list:
        print("No birthdays saved.")
        return

    print("\nSaved Birthdays:")
    for birthday in birthday_list:
        print(
            birthday["name"],
            "-",
            birthday["day"],
            "/",
            birthday["month"],
            "/",
            birthday["year"]
        )

def search_birthday(birthday_list, name):
    found = False
    for birthday in birthday_list:
        if birthday["name"].lower() == name.lower():

            print("\nbirthday found!")

            print(
                birthday["name"],
                "-",
                birthday["day"],
                "/",
                birthday["month"],
                "/",
                birthday["year"]
            )


            found = True
            break

    if not found:
        print("\nbirthday not found.")
            