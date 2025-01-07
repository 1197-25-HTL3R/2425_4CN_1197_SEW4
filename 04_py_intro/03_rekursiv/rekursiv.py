from typing import List


def M(n) -> int:
    if n > 100:
        return [n] + M(n-10)
    else:
        return [n] + M(M(n+11))

