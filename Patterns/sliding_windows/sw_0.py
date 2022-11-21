import math 


# Average of sliding window
def f(arr: list) -> list:
    return [sum(arr[i:i+5]) / 5 for i in range(len(arr)-4)]



