def reverse_sequence(array, start, stop):
    if start < stop - 1: # if at least two elements
        array[start], array[stop-1] = array[stop-1], array[start]
        reverse_sequence(array, start+1, stop-1)
