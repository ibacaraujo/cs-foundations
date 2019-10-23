# attempt
def reverse_list(data):
  data_str = ''.join(str(e) for e in data)
  data_str_reversed = data_str[::-1]
  reversed_list = list(data_str_reversed)
  reversed_list = list(map(int, reversed_list))
  
# exploring
def reverse_list_copy(data):
  length = len(data)
  reversed_list = [None] * length
  for i in range(length):
    reversed_list[length - 1 - i] = data[i]
  return reversed_list

def reverse_list_in_place(data):
  i = 0
  l = len(data)
  while i < l // 2:
    data[i], data[l-1-i] = data[l-1-i], data[i]
    i += 1
  return (data)
