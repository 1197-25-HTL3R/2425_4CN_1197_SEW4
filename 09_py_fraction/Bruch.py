__author__ = 'Danijel Stamenkovic'

def __init__(self, z=0, n=1):
    if n == 0:
        raise ValueError('n cannot be zero')
    self.z = int(z)
    self.n = int(n)



