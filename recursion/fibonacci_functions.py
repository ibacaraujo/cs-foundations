import time

# Define computation for the nth Fibonacci number using binary recursion
def bad_fibonacci(n):
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n-2) + bad_fibonacci(n-1)

# Use case for the bad_fibonacci function
start = time.time()
print("The 35th Fibonacci number is :", bad_fibonacci(35))
end = time.time()
print("It ellapsed", (end-start)%60, "seconds to compute it with the bad function.")

# Define computation for the nth Fibonnaci number using linear recursion
def good_fibonacci(n):
    if n <= 1:
        return (n,0)
    else:
        (a, b) = good_fibonacci(n-1)
        return (a+b, a)

# Use case for the good_fibonacci function
start = time.time()
print("The 35th Fibonacci number is:", good_fibonacci(35)[0])
end = time.time()
print("It ellapsed", (end-start)%60, "seconds to compute it with the good function.")
