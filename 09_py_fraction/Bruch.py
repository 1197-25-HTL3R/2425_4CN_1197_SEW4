__author__ = 'Danijel Stamenkovic'

class Bruch:

    def __init__(self, z=0, n=1):
        if n == 0:
            raise ValueError('n cannot be zero')
        self.z = int(z)
        self.n = int(n)

    def __str__(self):
        return f"{self.z}/{self.n}"

    def add(self, b):
        z = self.z * b.n + b.z * self.n
        n = self.n * b.n
        return Bruch(z, n)

    def sub(self, b):
        z = self.z * b.n - b.z * self.n
        n = self.n * b.n
        return Bruch(z, n)

    def mult(self, b):
        z = self.z * b.z
        n = self.n * b.n
        return Bruch(z, n)

    def div(self, b):
        z = self.z * b.n
        n = self.n * b.z
        return Bruch(z, n)

    @staticmethod
    def ggt(a:int, b:int):
        if a == 0 or b == 0:
            return 1

        while True:
            r = a / b
            if r == 0:
                return b
            a = b
            b = r



