from typing import List, Tuple


def collatz(n: int) -> List[int]:
    """
    Berechnet die Collatz-Sequenz für die gegebene Startzahl iterativ.

    >>> collatz(6)
    [6, 3, 10, 5, 16, 8, 4, 2, 1]
    >>> collatz(1)
    [1]
    >>> collatz(19)
    [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    ret = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        ret.append(n)
    return ret


def collatz_sequence(number: int) -> List[int]:
    """
    Berechnet die Collatz-Sequenz für die gegebene Startzahl rekursiv.

    >>> collatz_sequence(6)
    [6, 3, 10, 5, 16, 8, 4, 2, 1]
    >>> collatz_sequence(1)
    [1]
    >>> collatz_sequence(19)
    [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    >>> collatz_sequence(4)
    [4, 2, 1]
    """
    if number == 1:
        return [1]
    if number == 4:
        return [4, 2, 1]
    if number % 2 == 0:
        return [number] + collatz_sequence(number // 2)
    else:
        return [number] + collatz_sequence(number * 3 + 1)


def longest_collatz_sequence(n: int) -> Tuple[int, int]:
    """
    Findet die Zahl ≤ n mit der längsten Collatz-Sequenz und gibt diese sowie die Länge zurück.

    >>> longest_collatz_sequence(10)
    (9, 20)
    >>> longest_collatz_sequence(20)
    (19, 21)
    >>> longest_collatz_sequence(100)
    (97, 119)
    """
    res = [0, 0]
    for i in range(1, n + 1):
        if len(collatz_sequence(i)) > res[1]:
            res[0] = i
            res[1] = len(collatz_sequence(i))
    return tuple(res)


if __name__ == "__main__":
    assert collatz(6) == [6, 3, 10, 5, 16, 8, 4, 2, 1]
    assert collatz(1) == [1]
    assert collatz(19) == [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]

    assert collatz_sequence(6) == [6, 3, 10, 5, 16, 8, 4, 2, 1]
    assert collatz_sequence(1) == [1]
    assert collatz_sequence(19) == [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    assert collatz_sequence(4) == [4, 2, 1]

    assert longest_collatz_sequence(10) == (9, 20)
    assert longest_collatz_sequence(20) == (18, 21)
    assert longest_collatz_sequence(100) == (97, 119)

    print("Alle Tests erfolgreich!")
