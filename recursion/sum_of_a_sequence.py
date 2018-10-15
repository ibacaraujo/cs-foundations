def sum_sequence(array, n):
    # the base case
    if n == 0:
        return 0
    else:
        print(array[n-1])
        return array[n-1] + sum_sequence(array, n-1)

print(sum_sequence([1,2,3,4], 4))
