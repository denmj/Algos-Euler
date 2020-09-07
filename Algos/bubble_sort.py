
arr = [64, 34, 25, 12, 22, 11, 90]
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        print("i", i)
        for j in range(0, n - i - 1):
            print("j", j)
            pass
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[i]


print(arr)