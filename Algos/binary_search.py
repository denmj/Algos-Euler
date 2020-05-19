# binary search in sorted array


def binary_search(arr, left, right, x):

    if right >= left:
        mid = left + (right - left) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, left, mid-1, x)
        else:
            return binary_search(arr, mid+1, right, x)
        print(left, right, mid)
    else:
        return -1


arr = [2,3,4,10,40,50]

binary_search(arr,0, len(arr)-1, 10)
