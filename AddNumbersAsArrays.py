###Algorithm to add two numbers represented as arrays
# n1 = [1, 2, 3]; n2 = [4, 5, 6]
#res  = [5, 7, 9]

def addNumberArrays(a1, a2):
  res = []
  assert len(a1) == len(a2)

  N = len(a1)
  carry = 0
  for i in range(N-1, -1, -1):
    tempSum = a1[i] + a2[i] + carry
    if tempSum > 10:
      carry = 1
      res.append(tempSum % 10)
    else:
      res.append(tempSum)

  if carry == 1:
    res.append(1)

  res.reverse()
  return res


if __name__ == "__main__":
  a1 = [5, 7, 9]
  a2 = [6, 8, 9]
  print a1
  print a2

  print addNumberArrays(a1, a2)





