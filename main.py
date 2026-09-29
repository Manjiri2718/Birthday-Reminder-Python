from datetime import date
from file_handler import load_birthdays, save_birthdays

birthdays = load_birthdays()

while True:

    print("\n********************************")
    print("        # BIRTHDAY REMAINDER #    ")
    print("**********************************")
    print("1. Add birthday")
    print("2. View All Birthdays")
    print("3. Search Birthday")
    print("4. show Upcoming Birthdays")
    print("5.Exit")
    print("**********************************")

    choice = input("Enter your choice: ")

    # --------------------------------
    # 1. ADD BIRTHDAY
    # --------------------------------
    if choice == "1":

        print("\n=============ADD BIRTHDAY===========")

        name = input("Enter name: ")

        day = int(input("Enter birth day:"))
        month = int(input("Enter birth month: "))
        year = int(input("Enter birth year: "))

        birthday = {
            "name": name,
            "day": day,
            "month": month,
            "year": year
        }

        birthdays.append(birthday)

        save_birthdays(birthdays)

        print("\nBirthday added successfully!")


    # -------------------------------------
    # 2. VIEW ALL
    #--------------------------------------   
    elif choice =="2":

        print("\n============ ALL Birthdays ========")

        if len(birthdays) == 0:

                print("No birthdays saved.")

        else:
            for birthday in birthdays:
                print(birthday["name"], "->",
                                birthday["day"],
                                "/",
                                birthday["month"],
                                "/",
                                birthday["year"])


    #--------------------------------
    # 3. SEARCH
    #--------------------------------
    
    elif choice == "3":

        print("\n============ SEARCH BIRTHDAY ========")

        search_name = input("Enter name to search: ")

        found = False

        for birthday in birthdays:
            if birthday["name"].lower() == search_name.lower():
                print(birthday["name"], "->",
                      birthday["day"],
                      "/",
                      birthday["month"],
                      "/",
                      birthday["year"])
                found = True
                break

        if not found:
            print("Birthday not found.")


    #---------------------------------
    # 4. UPCOMING BIRTHDAYS
    #---------------------------------
    
    elif choice == "4":

        print("\n============ UPCOMING BIRTHDAYS ========")


        if len(birthdays) == 0:

            print("No birthdays saved.")

        else:

            today = date.today()
            found_upcoming = False

            for birthday in birthdays:

                day = int(birthday["day"])
                month = int(birthday["month"])


                next_birthday = date(
                    today.year,
                    month,
                    day
                )

                if next_birthday < today:

                    next_birthday = date(
                        today.year + 1,
                        month,
                        day
                    )

                days_remaining = (next_birthday - today).days

                if days_remaining == 0:
                    found_upcoming = True


                    print(
                        "🎂",
                        birthday["name"],
                        "has a birthday today! 🎉"
                    )
                elif days_remaining <= 30:
                    found_upcoming = True

                    print(
                        "🎂",
                        birthday["name"],
                        "has a birthday in",
                        days_remaining,
                        "days! 🎉"
                    )

            if not found_upcoming:
                print("No upcoming birthdays in the next 30 days.")



    #---------------------------
    # 5. EXIT
    #---------------------------
    elif choice == "5":
        print("\nThank you for using Birthday Reminder!")
        print("Exiting the program...")
        break

    else:
        print("Invalid choice. Please try again.")
