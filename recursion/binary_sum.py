# Define binary recursion function for computing the sum of a sequence
def binary_sum(array, start, stop):
    if start >= stop:
        return 0
    elif start == stop-1:
        return array[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(array, start, mid) + binary_sum(array, mid, stop)

# Use case
array = [1, 2, 3, 4]
print(binary_sum(array, 0, len(array)))
