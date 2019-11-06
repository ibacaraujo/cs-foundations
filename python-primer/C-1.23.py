# attempt
l = []
for i in range(10):
  l.append(i)
  try:
    l[i+1] = i + 1
  except IndexError:
    print("Don't try buffer overflow attacks in Python!")
