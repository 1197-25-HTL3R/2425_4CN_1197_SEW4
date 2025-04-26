__author__ = 'Danijel Stamenkovic'

class Fraction:

    def __init__(self, z=0, n=1):
        if n == 0:
            raise ValueError('n cannot be zero')

        if n < 0:
            z, n = -z, n

        self.z = int(z)
        self.n = int(n)
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
        g = self.gcd(self.z, self.n)
        self.z //= g
        self.n //= g

    @property
    def z(self):
        return self.z

    @property
    def n(self):
        return self.n

    def __repr__(self):
        return f"Fraction({self.z}, {self.n})"

    def __str__(self):
        z, n = self._z, self._n
        if abs(z) >= n:
            ganz = z // n
            rest = abs(z) % n
            if rest:
                return f"{ganz} {rest}/{n}"
            return str(ganz)
        return f"{z}/{n}"

    def __add__(self, b):
        if isinstance(b, int):
            other = Fraction(b)
        if isinstance(b, Fraction):
            z = self.z * b.n + b.z * self.n
            n = self.n * b.n
            return Fraction(z, n)
        return NotImplemented

    def _radd__(self, b):
        return self.__add__(b)

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
            other = Fraction(b)
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