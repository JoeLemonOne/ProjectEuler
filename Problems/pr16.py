"""
215 = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.
Какова сумма цифр числа 21000?
"""


number = 2
for i in range(100):
    number *= number
    print(i)
print(number)