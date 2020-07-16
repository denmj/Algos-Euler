"""
Given array of integers, remove each kth element from it.
"""
k = 1
inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resArray = []

counter = 0
for i in range(len(inputArray)):
    if counter != k-1:
        resArray.append(inputArray[i])
        counter += 1
    else:
        counter = 0
