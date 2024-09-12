numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
x = 0
for i in numbers[1:15]:
    for j in range(2, i):
        if i % j == 0:
            x = x + 1

    if x > 0:
        not_primes.append(i)
        x = 0
    else:
        primes.append(i)

print('Простые числа: ', primes)
print('Непростые числа: ', not_primes)
