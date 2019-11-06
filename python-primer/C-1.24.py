# attempt
def count_vowels(string):
  count = 0
  for c in string:
    if c in ['a', 'e', 'i', 'o', 'u']:
      count += 1
  return count
