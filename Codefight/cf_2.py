def centuryFromYear(year):
    reminder = year % 100
    if reminder != 0:
        return (year//100)+1
    else:
        return year//100

