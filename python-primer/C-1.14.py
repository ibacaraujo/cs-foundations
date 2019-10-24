# attempt!
def my_product_odd(numbers):
  for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
      if (numbers[i] * numbers[j]) % 2 != 0:
        return True
  return True
