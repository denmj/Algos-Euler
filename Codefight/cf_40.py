"""
Given a string, ooutput its loongest prefix which contains only digits

Example: for inputString = "123aa1"

longestDigitPrefix(inputString)  = "123"

"""
import string

example_str = "123aa1"
example_str_2 = "sdad1231"


def longestDigitsPrefix(inputString):
    empty_str = ""
    for e in example_str:
        if not e.isdigit():
            print("")
            break
        elif e.isdigit():
            empty_str += e


