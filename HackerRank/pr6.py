"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note : Midnight is 12:00:00 AM on a 12-hour clock and 00:00:00 on a 24-hour clock.
 Noon is 12:00:00 PM on 12-hour clock and 12:00:00 on 24-hour clock.
"""


def timeConversion(str1):
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2: -2]

    elif str1[-2:] == "AM":
        return str1[:-2]

    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]

    else:
        return str(int(str1[:2]) + 12) + str1[2:8]

s = "07:05:45PM"

