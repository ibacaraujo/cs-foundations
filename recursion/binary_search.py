# Define function

def binary_search(array, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == array[mid]:
            return True
        else:
            if target < array[mid]:
                return binary_search(array, target, low, mid - 1)
            else:
                return binary_search(array, target, mid + 1, high)

# Use case
array = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
target = 22
result = binary_search(array, target, 0, len(array))
if (result):
    print(str(target) + " is in the array!")
else:
    print(str(target) + " was not found in the array.")
