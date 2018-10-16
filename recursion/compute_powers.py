# Define functions to Recursive Algorithms for Computing Powers
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)

def power2(x, n):
    if n == 0:
        return 1
    else:
        partial = power2(x, n // 2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result

# Use cases
print(power(2,2))
print(power2(2,2))
