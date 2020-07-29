
def pr3(n):
    if n % 2 != 0:
        print("Wierd")
    elif n % 2 == 0 and n in range(2, 6):
        print("Not Weird")
    elif n % 2 == 0 and n in range(6, 21):
        print("Wierd")
    elif n % 2 == 0 and n > 20:
        print("Not Wierd")


