"""
Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
Найдите сумму всех простых чисел меньше двух миллионов.
"""

def prime_check(x,X):
    a = 0
    for el in X:
        #print(x,el)
        if x % el == 0:
            a += 1
    if a == 0:
        return x


n = 1
prime = [2,3]

while 6 * n - 1 < 2000000:
    x = prime_check(6 * n - 1 , prime)
    if x:
        prime.append(x)
    x = prime_check(6 * n + 1, prime)
    if x:
        prime.append(x)
    n += 1

print(prime)
sum(prime)
print(sum(prime))
