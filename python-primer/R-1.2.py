# attempt
def is_even(n):
  return not int(f'{n:08b}'[-1])
  
# exploring
def is_even(n):
  return not (n & 1)
