"""
Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?
"""

number = 600851475143
d_max = 1
i = 2

while number != 1:
    if number % i == 0:
        if d_max < i:
            d_max = i
        number = int(number / i)
    i += 1

print(d_max)