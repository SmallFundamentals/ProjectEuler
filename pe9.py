import math

def main():
    perfSq = []

    i = 1
    while(i <= 1000):
        perfSq.append(i**2)
        i+=1

    for i in perfSq:
        for j in perfSq:
            if (1000 - math.sqrt(i) - math.sqrt(j))**2 in perfSq:
                if i + j == (1000 - math.sqrt(i) - math.sqrt(j))**2:
                    print(math.sqrt(i))
                    print(math.sqrt(j))
                    print(1000-math.sqrt(i)-math.sqrt(j))
                    print(math.sqrt(i) * math.sqrt(j) * (1000-math.sqrt(i)-math.sqrt(j)))
                    return 1

main()
