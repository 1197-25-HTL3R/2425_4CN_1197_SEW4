import collections
from collections.abc import Collection
from typing import List

class Caesar:
    """
    Eine Klasse zur Durchführung der Caesar-Verschlüsselung.
    """

    @staticmethod
    def to_lowercase_letter_only(plaintext: str) -> str:
        """
        Wandelt den gegebenen Text in Kleinbuchstaben um und entfernt alle Nicht-Buchstaben.

        >>> Caesar.to_lowercase_letter_only("Hello, World!")
        'helloworld'
        >>> Caesar.to_lowercase_letter_only("Python 3.9")
        'python'
        """
        ret = plaintext.lower()
        return "".join(i for i in ret if i.isalpha())

    @staticmethod
    def encrypt(plaintext: str, key: str = None) -> str:
        """
        Verschlüsselt den gegebenen Text mit dem angegebenen Schlüssel.

        >>> Caesar.encrypt("hello", "b")
        'jgnnq'
        >>> Caesar.encrypt("hello")
        'hello'
        """
        if key is None:
            return Caesar.to_lowercase_letter_only(plaintext)
        else:
            text = Caesar.to_lowercase_letter_only(plaintext)
            ret = ""
            for c in text:
                letter = ord(c) - ord('a')
                shift = ord(key) - ord('a')
                ret += chr(((letter + shift) % 26) + ord('a')+1)
            return ret

    @staticmethod
    def decrypt(plaintext: str, key: str = None) -> str:
        """
        Entschlüsselt den gegebenen Text mit dem angegebenen Schlüssel.

        >>> Caesar.decrypt("jgnnq", "b")
        'hello'
        >>> Caesar.decrypt("hello")
        'hello'
        """
        if key is None:
            return Caesar.to_lowercase_letter_only(plaintext)
        else:
            text = Caesar.to_lowercase_letter_only(plaintext)
            ret = ""
            for c in text:
                letter = ord(c) - ord('a')
                shift = ord(key) - ord('a')
                ret += chr(((letter - shift + 26) % 26) + ord('a')-1)
            return ret

    @staticmethod
    def crack(crypttext: str, elements: int = 1) -> List[str]:
        """
        Knackt die Caesar-Verschlüsselung und gibt die häufigsten Buchstaben zurück.

        >>> Caesar.crack("jgnnq", 2)
        ['n', 'g']
        >>> Caesar.crack("hello world", 2)
        ['l', 'o']
        """
        letters = {
            'e': 17.40, 'n': 9.78, 'i': 7.55, 's': 7.27, 'r': 7.00,
            'a': 6.51, 't': 6.15, 'd': 5.08, 'h': 4.76, 'u': 4.35,
            'l': 3.44, 'c': 3.06, 'g': 3.01, 'm': 2.53, 'o': 2.51,
            'b': 1.89, 'w': 1.89, 'f': 1.66, 'k': 1.21, 'z': 1.13,
            'p': 0.79, 'v': 0.79, 'j': 0.27, 'y': 0.04, 'x': 0.03,
            'q': 0.02
        }

        counter = {char: 0 for char in 'abcdefghijklmnopqrstuvwxyz'}

        for i in crypttext:
            if i.isalpha():
                counter[i] += 1

        counter_sorted = sorted(counter.items(), key=lambda item: item[1], reverse=True)
        list_counter = [key for key, value in counter_sorted]
        return list_counter[:elements]


    import doctest

    if __name__ == "__main__":
        doctest.testmod()








