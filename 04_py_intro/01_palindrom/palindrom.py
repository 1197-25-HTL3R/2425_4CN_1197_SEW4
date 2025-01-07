def is_palindrom(s: str) -> bool:
    """
    Prüft, ob ein String ein Palindrom ist.

    >>> is_palindrom("abba")
    True
    >>> is_palindrom("abc")
    False
    """
    return s == s[::-1]

def is_palindrom_sentence(s: str) -> bool:
    """
    Prüft, ob ein Satz ein Palindrom ist, indem Leerzeichen und Satzzeichen ignoriert werden.

    >>> is_palindrom_sentence("Was it a car or a cat I saw?")
    True
    >>> is_palindrom_sentence("Hello, World!")
    False
    """
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]

def is_palindrom_product(x: int) -> int:
    """
    Findet das größte Palindromprodukt von zwei dreistelligen Zahlen kleiner als x.

    >>> is_palindrom_product(9000)
    8998
    >>> is_palindrom_product(10000)
    9999
    """
    for number in range (x-1, 0, -1):
        for number2 in range (x-1, 0, -1):
            product = number * number2
            if is_palindrom(str(product)) and product < x:
                return product
    return -1

def get_dec_hex_palindrom(x: int) -> int:
    """
    Findet die größte Zahl kleiner als x, die sowohl im Dezimal- als auch im Hexadezimalsystem ein Palindrom ist.

    >>> get_dec_hex_palindrom(1000)
    979
    >>> get_dec_hex_palindrom(2000)
    1991
    """
    for number in range (x-1, 0, -1):
        if is_palindrom(str(number)) and is_palindrom(to_base(number, 16)):
            return number
    return -1

def to_base(number: int, base: int) -> str:
    """
    Wandelt eine Zahl im Dezimalsystem in eine Zahl im gewünschten Zielsystem um.

    >>> to_base(1234, 16)
    '4D2'
    >>> to_base(255, 16)
    'FF'
    """
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ret = ""
    while number > 0:
        ret = chars[number % base] + ret
        number //= base
    return ret

if __name__ == "__main__":
    import doctest
    doctest.testmod()
