# attempt
def choice(data):
  minimum = min(data)
  maximum = max(data)
  result = None
  while result not in data:
    result = random.randrange(minimum, maximum + 1)
  return result
  
# exploring
def choice(data):
  return data[random.randrange(0, len(data))]
