import time

# Define computation for the nth Fibonacci number using binary recursion

def bad_fibonacci(n):
    if n <= 1:
        return n
    else:
        return bad_fibonacci(n-2) + bad_fibonacci(n-1)
start = time.time()
# Use case for the bad_fibonacci function
print("The 35th Fibonacci number is :", bad_fibonacci(35))
end = time.time()
print("It ellapsed", (end-start)%60, "seconds to compute it with the bad function.")
