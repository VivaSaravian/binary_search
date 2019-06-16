def binary_search(arr, target):
    mid = len(arr) // 2
    low = 0
    high = len(arr) - 1
    while low <= high and arr[mid] != target:
        if target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    if target == arr[mid]:
        return mid
    else:
        return None


arr = []
arr.sort()
while True:
    try:
        n = int(input())
        if n:
            arr.append(n)
    except:
        break



