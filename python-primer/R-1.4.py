# attempt
def squares_sum(n):
  result = 0
  for i in range(n):
    result += i ** 2
  return result
  
# exploring
def sum_of_squares(n):
  return sum((i * i) for i in range(n) if (n > 0))

if __name__ == '__main__':
  print(sum_of_squares(5))
