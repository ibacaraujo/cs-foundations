def binary_sum(array, start, stop):
    if start >= stop:
        return 0
    elif start == stop-1:
        return array[start]
    else:
        mid = (start + stop) // 2
        return binary_sum(array, start, mid) + binary_sum(array, mid, stop)
