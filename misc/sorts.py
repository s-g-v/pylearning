#!/usr/bin/env python3

import random


def _print_decorator(func):
    def decorated_func(src):
        print(func.__name__.capitalize() +" sort")
        print("Source list " + str(src))
        result = func(src)
        print("Result list " + str(result) + "\n")
    return decorated_func


def _random_list(len, min=-10, max=10):
    result=[]
    for i in range(len):
        result.append(random.randint(min,max))
    return result


@_print_decorator
def buble(to_sort):
    src = list(to_sort)
    for n in range(1,len(src)):
        for i in range(len(src)-n):
            if src[i] > src[i+1]:
               src[i],src[i+1]=src[i+1],src[i]
    return src


@_print_decorator
def select(to_sort):
    src = list(to_sort)
    for i in range(len(src)):
        n = i + 1
        while n < len(src):
            if src[n] < src[i]:
                src[n],src[i] = src[i],src[n]
            n+=1
    return src


@_print_decorator
def insert(to_sort):
    src = list(to_sort)
    for i in range(1, len(src)):
        while i > 0 and src[i - 1] > src[i]:
            src[i - 1], src[i] = src[i], src[i - 1]
            i-=1
    return src


def fib(n):
    x = 1
    y = 1
    for i in range (2, n):
        y = x + y
        x = y - x
    print("Fibonachi number #" + str(n) + " is " + str(y))


if __name__=="__main__":
    l = _random_list(10)
    buble(l)
    select(l)
    insert(l)
