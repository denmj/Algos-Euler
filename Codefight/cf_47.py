"""
A media access control address (MAC address) is a unique identifier assigned to network interfaces
for communications on the physical network segment.

The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly
form is six groups of two hexadecimal digits (0 to 9 or A to F), separated by hyphens
(e.g. 01-23-45-67-89-AB).

Your task is to check by given string inputString whether it
corresponds to MAC-48 address or not.


For inputString = "00-1B-63-84-45-E6", the output should be
isMAC48Address(inputString) = true;
For inputString = "Z1-1B-63-84-45-E6", the output should be
isMAC48Address(inputString) = false;
For inputString = "not a MAC-48 address", the output should be
isMAC48Address(inputString) = false.

"""

str_1 = "0-1B-63-84-45-E6"
str_2 = "Z1dasd6"


def imac_adress(input_str):
    l = input_str.split("-")
    if len(l) != 6:
        return False
    for i in l:
        if len(i) != 2:
            return False
        try:
            int(i, 16)
        except:
            return False
    return True
