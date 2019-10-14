# attempt
def minimax(data):
  smallest = data[0]
  largest = data[0]
  for i in range(1, len(data)):
    if smallest > data[i]:
      smallest = data[i]:
    if largest < data[i]:
      largest = data[i]
  return (smallest, largest)
  
# exploring
def minimax(*data):
  return (*data, *data) if len(data) == 1 else (min(data), max(data))
  
if __name__ == '__main__':
  print(minimax(4, 100, 10, 1))
