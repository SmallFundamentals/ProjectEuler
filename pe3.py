# coding: utf-8

import math

def FermatFactor(n): # n should be odd
  a = math.sqrt(n)
  a = math.ceil(a)
  bSqrd = a*a - n
  while math.sqrt(bSqrd) != math.floor(math.sqrt(bSqrd)):
    a = a + 1 # equivalently: b2 ← b2 + 2*a + 1
    bSqrd = a*a - n  # a ← a + 1
  return [a, math.sqrt(bSqrd)]
  
def main():
  l = list()
  l.append(600851475143)
  
  while True:
    l.sort()
    res = FermatFactor(l.pop(-1))
    f1 = res[0] + res[1]
    f2 = res[0] - res[1]
    if f2 == 1:
      break
    else:
      print "N = " + str(f1*f2)
      print "f1 = " + str(f1)
      print "f2 = " + str(f2)
      l.append(f1)
      l.append(f2)
  print f1
  
main()