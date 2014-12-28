PRIMES = [2, 3, 5, 7, 11, 13, 17, 19]

def primeFactorization(n):
  print n
  l = list()
  if n == 1 or n == 0:
    return l
  else:
    idx = -1
    while(n % PRIMES[idx] != 0):
      idx = idx -1
    l = primeFactorization(n / PRIMES[idx])
    l.append(PRIMES[idx])
    return l

def arraylize(n):
  tot = [0]*20
  
  l = primeFactorization(n)
  for j in xrange(len(l)):
    tot[l[j]] = tot[l[j]] + 1
      
  return tot
      
  
def main(n):
  
  result = [0] * 20
  for i in xrange(n):
    listResult = arraylize(i)
    for j in xrange(len(listResult)):
      if listResult[j] > result[j]:
        result[j] = listResult[j]
  
  ret = 1
  
  for prime in PRIMES:
    if result[prime] == 0:
      continue
    ret = ret * prime ** result[prime]  
    
  print ret
  
main(20)