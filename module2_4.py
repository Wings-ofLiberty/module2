numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    c = 0
    for j in range (1,i):
            if i % j == 0:
                c = (c+1)
    if c == 1:
        primes.append(i)
    else:
        if i > 1:
            not_primes.append(i)

print (primes)
print (not_primes)














