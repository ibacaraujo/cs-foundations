# attempt
def array_product(a, b):
  c = [0] * len(a)
  for i in range(len(a)):
    c[i] = a[i] * b[i]
  return c
