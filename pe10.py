def sieve(n):
    ret = [1] * n
    ret[0] = 0
    ret[1] = 0
  
    for i in range(n):
        if ret[i] == 0:
            continue
        else:
            for j in range(i+i, n, i):
                ret[j] = 0
  
    return ret
  
def main(n):
    array = sieve(n)

    total = 0
  
    for i in range(len(array)):
        if array[i] == 1:
            total += i
    print(total)

main(2000001)
