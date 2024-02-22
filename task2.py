import numpy as np


def fibonacci(n):

    fibo_series = [0 , 1]

    for i in range(2 , n):
        next_num = fibo_series[-1] + fibo_series[-2]
        fibo_series.append(next_num)

    return fibo_series[:n]

print(fibonacci(10))
