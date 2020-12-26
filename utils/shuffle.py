from random import randint


def shuffle(lst, n=1):
    if n > 20:
        raise MemoryError('Too many iterations')

    length = len(lst) - 1

    for i in range(n):
        for j in range(length):
            rand = randint(0, length)
            lst[j], lst[rand] = lst[rand], lst[j]

    return lst


# print(shuffle(['a', 'b', 'c', 'd'], 10))
