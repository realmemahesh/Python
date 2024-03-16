def pair_1(n):
  total = 0
  for i in range(n):
    total = total + pair_2(i,i+1)
  return total


def pair_2(a,b):
  return a + b

pair_1(4)