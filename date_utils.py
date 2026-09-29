from datetime import date


def get_upcoming_birthdays(birthdays):
    today = date.today()
    upcoming_birthdays = []

    for birthday in birthdays:
        day = int(birthday["day"])
        month = int(birthday["month"])

        next_birthday = date(today.year, month, day)

        if next_birthday < today:
            next_birthday = date(today.year + 1, month, day)

        days_remaining = (next_birthday - today).days

        if days_remaining == 0:
            upcoming_birthdays.append(
                f"🎂 {birthday['name']} has a birthday today! 🎉"
            )
        elif days_remaining <= 30:
            upcoming_birthdays.append(
                f"🎂 {birthday['name']} has a birthday in {days_remaining} days! 🎉"
            )

    return upcoming_birthdays