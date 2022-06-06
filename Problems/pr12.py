n = 0
number = 0
max_dividers = [1, 1]
div_start = [1,1 ]


def dividers_test(x):
    global dividers
    for i in range(int(x / 2)):
        if x % (i + 1) == 0:
            dividers += 1


while max_dividers[1] <= 500: