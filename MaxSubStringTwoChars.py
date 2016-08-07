##Given a string s find the maximal length substring with only 2 unique characters
## e.g s = "abcabbac", the res="abba"

def longestTwoCharSubstring(s):
  n = len(s)

  if n < 2:
    return None

  charSet = set()
  left = 0; right = 0

  i = 0; j = 0

  while j < n:
    char = s[j]
    if len(charSet) == 2:
      if char in charSet:
        j = j + 1
        
        if j - i > right - left:
          left = i
          right = j
      else:
        charSet.clear()
        j = j - 1
        i = j
        charSet.add(s[i])
        j = j + 1
    else:
      charSet.add(char)
      j = j + 1
      if j - i > right - left:
        left = i
        right = j

  return s[left:right]

if __name__ == "__main__":
  s = raw_input()
  print "MaxSubstr: ", longestTwoCharSubstring(s)
