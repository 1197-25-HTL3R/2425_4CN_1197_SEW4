from typing import List, Tuple


def collatz(n) -> list:
    ret = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    ret.append(n)
    return ret


def collatz_sequence(number: int) -> List[int]:
    if number == 1:
        return [1]

    if number == 4:
        return [4,2,1]

    if number % 2 == 0:
        return [number] + collatz_sequence(number // 2)
    else:
        return [number] + collatz_sequence(number*3+1)

def longest_collatz_sequence(n: int) -> Tuple[int, int]:
    res = [0,0]
    for i in range (1, n+1):
        if len(collatz_sequence(n)) > res[1]:
            res[0] = i
            res[1] = len(collatz_sequence(n))
    return tuple(res)
