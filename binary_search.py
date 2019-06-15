def binary_search(arr, target):
    mid = len(a) // 2
    low = 0
    high = len(a) - 1
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


a = [1,2,3,4,5,6,7,8,9,10]
