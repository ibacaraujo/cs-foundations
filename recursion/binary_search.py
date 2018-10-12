def binary_search(array, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == array[mid]:
            return True
        else:
            if target < array[mid]:
                binary_search(array, target, low, mid - 1)
            else:
                binary_search(array, target, mid + 1, high)
