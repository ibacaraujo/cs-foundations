# attempt
def sum_of_squares(n):
  result = 0
  for i in range(n):
    if (i % 2 != 0):
      result += i ** 2
  return result
  
  # exploring
  def sum_of_squares_of_odd_positive_integers(n):
    return sum((i * i) for i in range(1, n, 2))
