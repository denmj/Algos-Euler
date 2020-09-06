# Linear search
def search(arr, n, x):
    for i in range(n):
        if arr[i] == x:
            return i
    return -1


a = [1, 10, 30, 15]
x = 30
n = len(a)

# Worst Case Analysis  O(n)
print(x, "is present at index",
      search(a, n, x))


