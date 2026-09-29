def valid_name(name):
    if not name.strip():
        return False
    return True

def valid_day(day):
    if not day.isdigit():
        return False
    day = int(day)
    if day < 1 or day > 31:
        return False
    return True

def valid_month(month):
    if not month.isdigit():
        return False
    month = int(month)
    if month < 1 or month > 12:
        return False
    return True

def valid_year(year):
    if not year.isdigit():
        return False
    year = int(year)
    if year < 1900 or year > 2100:
        return False
    return True