import random
import time


def fib_sequence(number):

    start = time.perf_counter()
    fib_list = [None] * (number + 1)

    fib_list[0] = 0

    for i in range(1, len(fib_list)):
        fib_list[i] = i

    for i in range(1, len(fib_list) - 1):
        fib_list[i + 1] = fib_list[i] + fib_list[i - 1]

    end = time.perf_counter()
    comp_time = (end - start)

    print("fib({}) = {}".format(number, fib_list[len(fib_list) - 1]))
    print("fib({}) took {} seconds".format(number, comp_time))


rand_num = random.randrange(15, 35)

fib_sequence(rand_num)
