# attempt
def sum_of_odds(n):
  return sum([k ** 2 for k in range(n) if k % 2 != 0])
  
# exploring
def sumoddsquares(k):
  return sum(x * x for x in range(1,k) if x % 2 == 1)
