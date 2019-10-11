# attempt
def is_multiple(n, m):
  if n % m == 0:
    return True
  return False
  
# exploring
def is_multiple(x, y):
  return x and (y % x) == 0
