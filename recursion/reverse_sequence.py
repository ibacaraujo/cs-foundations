# Define function for Reversing a Sequence with Recursion
def reverse_sequence(array, start, stop):
    if start < stop - 1: # if at least two elements
        array[start], array[stop-1] = array[stop-1], array[start]
        reverse_sequence(array, start+1, stop-1)
    return array

# Use case
array = [1, 2, 3, 4, 5, 6, 7, 8]
print("Reverse ", array, "is the following: ", reverse_sequence(array, 0, len(array)))
