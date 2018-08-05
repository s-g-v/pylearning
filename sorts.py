#!/usr/bin/env python3

import random
import time


def _print_decorator(func):
    def decorated_func(src):
        print(func.__name__.capitalize() + " sort")
        print("Source list " + str(src))
        result = func(src)
        print("Result list " + str(result) + "\n")
    return decorated_func


def _timer(func):
    def decorated_func(*args):
        start = time.time()
        result = func(*args)
        print("Calculation time: %.4f ms" % ((time.time() - start) * 1000))
        return result
    return decorated_func


def _random_list(length, min_val=-20, max_val=20):
    return [random.randint(min_val, max_val) for _ in range(length)]


@_print_decorator
@_timer
def buble(to_sort):
    arr = list(to_sort)
    for n in range(1, len(arr)):
        for i in range(len(arr)-n):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


@_print_decorator
@_timer
def select(to_sort):
    arr = list(to_sort)
    for i in range(len(arr)):
        n = i + 1
        while n < len(arr):
            if arr[n] < arr[i]:
                arr[n], arr[i] = arr[i], arr[n]
            n += 1
    return arr


@_print_decorator
@_timer
def insert(to_sort):
    arr = list(to_sort)
    for i in range(1, len(arr)):
        while i > 0 and arr[i - 1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1
    return arr


def fib(n):
    x, y = 0, 1
    for i in range(1, n):
        x, y = y, x + y
    print("Fibonachi number #" + str(n) + " is " + str(x))


def factorial(n):
    from functools import reduce
    return reduce(lambda x, y: x * y, range(1, n))


@_timer
def bitxor(M, N):
    arr = [i ^ (i+1) for i in range(M, N)]
    while len(arr) > 2:
        arr = [arr[i] ^ arr[i + 1] for i in range(len(arr) - 1)]
    return arr[0]


def bitxor_rec(M, N):
    if M == N:
        return 0
    if M == N-1:
        print(M, N, "=", M ^ N)
        return M ^ N
    avg = (M + N) // 2
    return bitxor_rec(M, avg) ^ bitxor_rec(avg + (M + N) % 2, N)


def f(a):
    res = [a, 1, a + 1, 0]
    return res[a % 4]


def getXor(a, b):
    return f(b) ^ f(a - 1)

if __name__ == "__main__":
    # l = _random_list(20)
    # buble(l)
    # select(l)
    # insert(l)
    print(bitxor(5, 11))
    print(bitxor_rec(5, 11))
