# My implementation of Summing the Elements of a Sequence Recursively
def sum_sequence(array, n):
    # the base case
    if n == 0:
        return 0
    # the recursive case
    else:
        return array[n-1] + sum_sequence(array, n-1)

# Use case
print(sum_sequence([1,2,3,4], 4))
