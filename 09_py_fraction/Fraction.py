import functools


@functools.total_ordering

class Fraction:

    """
    Klasse für Bruchzahlen

    Doctest-Beispiele:

    >>> b0 = Fraction()
    >>> repr(b0)
    'Fraction(0, 1)'
    >>> print(b0)
    0/1

    >>> b1 = Fraction(5)
    >>> repr(b1)
    'Fraction(5, 1)'

    >>> # Normales und gemischtes Format
    >>> b2 = Fraction(3, 2)
    >>> repr(b2)
    'Fraction(3, 2)'
    >>> print(b2)
    1 1/2

    >>> b3 = Fraction(-7, 3)
    >>> print(b3)
    -2 1/3

    >>> b4 = Fraction(2, 4)
    >>> repr(b4)
    'Fraction(1, 2)'

    >>> Fraction(1, 2) + Fraction(1, 4)
    Fraction(3, 4)
    >>> 1 + Fraction(2, 3)
    Fraction(5, 3)
    >>> Fraction(2, 3) + 1
    Fraction(5, 3)

    >>> # Subtraktion
    >>> Fraction(3, 4) - Fraction(1, 2)
    Fraction(1, 4)
    >>> 2 - Fraction(3, 4)
    Fraction(5, 4)

    >>> # Multiplikation
    >>> Fraction(2, 3) * Fraction(3, 4)
    Fraction(1, 2)
    >>> 3 * Fraction(1, 3)
    Fraction(1, 1)

    >>> # Division
    >>> Fraction(3, 4) / Fraction(1, 2)
    Fraction(3, 2)
    >>> 1 / Fraction(1, 4)
    Fraction(4, 1)

    >>> try:
    ...     Fraction(1, 2) / Fraction(0, 1)
    ... except ValueError as e:
    ...     print(type(e).__name__)
    ValueError

    >>> float(Fraction(3, 2))
    1.5
    >>> Fraction(3, 2).as_integer_ratio()
    (3, 2)

    >>> Fraction(1, 2) == Fraction(2, 4)
    True
    >>> Fraction(1, 2) < Fraction(2, 3)
    True
    >>> Fraction(4, 3) > Fraction(1, 1)
    True
    """

    def __init__(self, z=0, n=1):
        if n == 0:
            raise ValueError('n cannot be zero')

        if n < 0:
            z, n = -z, -n

        self._z = int(z)
        self._n = int(n)
        self._reduce()

    @staticmethod
    def gcd(a:int, b:int):
        if a == 0 or b == 0:
            return 1

        while True:
            r = a % b
            if r == 0:
                return b
            a = b
            b = r

    def _reduce(self):
        g = self.gcd(self._z, self._n)
        self._z //= g
        self._n //= g

    @property
    def z(self):
        return self._z

    @property
    def n(self):
        return self._n

    def __repr__(self):
        return f"Fraction({self.z}, {self.n})"

    def __str__(self):
        z, n = self._z, self._n
        if abs(z) >= n:
            whole = abs(z) // n * (1 if z > 0 else -1)
            rest = abs(z) % n
            if rest:
                return f"{whole} {rest}/{n}"
            return str(whole)
        return f"{z}/{n}"

    def __add__(self, b):
        if isinstance(b, int):
            b = Fraction(b)
        if isinstance(b, Fraction):
            z = self.z * b.n + b.z * self.n
            n = self.n * b.n
            return Fraction(z, n)
        return NotImplemented

    def __radd__(self, b):
        if isinstance(b, int):
            return self + b
        return NotImplemented

    def __sub__(self, b):
        if isinstance(b, int):
            b = Fraction(b)
        if isinstance(b, Fraction):
            z = self.z * b.n - b.z * self.n
            n = self.n * b.n
            return Fraction(z, n)
        return NotImplemented

    def __rsub__(self, b):
        if isinstance(b, int):
            return Fraction(b).__sub__(self)
        return NotImplemented

    def __mul__(self, b):
        if isinstance(b, int):
            b = Fraction(b)
        if isinstance(b, Fraction):
            return Fraction(self._z * b._z, self._n * b._n)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, b):
        if isinstance(b, int):
            b = Fraction(b)
        if isinstance(b, Fraction):
            if b._z == 0:
                raise ValueError('Division with zero')
            return Fraction(self._z * b._n, self._n * b._z)
        return NotImplemented

    def __rtruediv__(self, b):
        if isinstance(b, int):
            return Fraction(b).__truediv__(self)
        return NotImplemented

    def __eq__(self, b):
        if isinstance(b, int):
            b = Fraction(b)
        if isinstance(b, Fraction):
            return self._z * b._n == b._z * self._n
        return NotImplemented

    def __lt__(self, b):
        if isinstance(b, int):
            b = Fraction(b)
        if isinstance(b, Fraction):
            return self._z * b._n < b._z * self._n
        return NotImplemented

    def __float__(self):
        return self._z / self._n

    def as_integer_ratio(self):
        return self._z, self._n

    @z.setter
    def z(self, value):
        self._z = value

    @n.setter
    def n(self, value):
        self._n = value

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)