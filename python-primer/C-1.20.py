# attempt
def shuffle(data):
  result = []
  indexes = []
  while len(indexes) != len(data):
    index = randint(0, len(data) - 1)
    if index not in indexes:
      result.append(data[index])
      indexes.append(index)
  return result
