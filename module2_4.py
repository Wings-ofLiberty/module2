numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for selected_number in numbers:
    c = False
    for multiplier in range (1,selected_number):
            if selected_number % multiplier == 0:
                c = (c+1)
    if c == True:
        primes.append(selected_number)
    else:
        if selected_number > 1:
            not_primes.append(selected_number)

print (primes)
print (not_primes)














