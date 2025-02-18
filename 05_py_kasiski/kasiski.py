import collections
import itertools
from collections.abc import Collection
from typing import List, Set, Tuple


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
        'ifmmp'
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
                ret += chr(((letter + shift) % 26) + ord('a'))
            return ret

    @staticmethod
    def decrypt(plaintext: str, key: str = None) -> str:
        """
        Entschlüsselt den gegebenen Text mit dem angegebenen Schlüssel.

        >>> Caesar.decrypt("ifmmp", "b")
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
                ret += chr(((letter - shift) % 26) + ord('a'))
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


class Vigenere:

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
    def cncrypt(selfplaintext: str, key: str = None) -> str:

        """
        Verschlüsselt den gegebenen Text mit einem String-Key mithilfe der Viginere-Verschlüsselung
        :param key: (sich evtl. wiederholender) Verschlüsselungsstring
        :return: verschlüsselter Text

        >>> Vigenere.cncrypt("sigmaboy", "apfel")
        'sxlqlbdd'

        >>> Vigenere.cncrypt("sigmaboy", "aaaaa")
        'sigmaboy'
        """

        text = Vigenere.to_lowercase_letter_only(selfplaintext)
        ret = ""
        key_cycle = itertools.cycle(key)

        for i in text:

            if i.isalpha():
                ret += Caesar.encrypt(i, next(key_cycle))

        return ret

    @staticmethod
    def decrypt(selfplaintext: str, key: str = None) -> str:
        """
        Entschlüsselt einen mit dem Vigenere-Algorithmus verschlüsselten Text
        :param key: der (sich eventuell wiederholende) Entschlüsselungskey
        :return: entschlüsselter Plaintext

        >>> Vigenere.decrypt("sxlqlbdd", "apfel")
        'sigmaboy'

        >>> Vigenere.decrypt("sxqlbdd", "aaaaa")
        'sxqlbdd'
        """

        text = Vigenere.to_lowercase_letter_only(selfplaintext)
        ret = ""
        key_cycle = itertools.cycle(key)

        for i in text:

            if i.isalpha():
                ret += Caesar.decrypt(i, next(key_cycle))

        return ret


class Kasiski:
    def __init__(self, crypttext: str = ""):
        self.crypttext = Vigenere.to_lowercase_letter_only(crypttext)

    def allpos(self, text: str, teilstring: str) -> List[int]:
        """Berechnet die Positionen von teilstring in text.
        Usage examples:
        >>> k = Kasiski()
        >>> k.allpos("heissajuchei, ein ei", "ei")
        [1, 10, 14, 18]
        >>> k.allpos("heissajuchei, ein ei", "hai")
        []"""

        ret = []
        start = 0

        while True:
            pos = text.find(teilstring, start)
            if pos == -1:
                break
            ret.append(pos)
            start = pos + 1

        return ret

    def alldist(self, text:str, teilstring:str) -> Set[int]:
        """Berechnet die Abstände zwischen allen Vorkommnissen des Teilstrings im verschlüsselten Text
        und gibt diese sortiert zurück.
        Usage examples:
        >>> k = Kasiski()
        >>> k.alldist("heissajuchei, ein ei", "ei")
        {4, 8, 9, 13, 17}
        >>> k.alldist("heissajuchei, ein ei", "hai")
        set()"""

        ret = set()
        positions = self.allpos(text, teilstring)

        num = itertools.cycle(positions)

        for i in positions:
            cycle_end = len(positions)
            while cycle_end > 0:
                ret.add(abs(next(num)-i))
                cycle_end -= 1

        ret = {x for x in ret if x != 0}

        return ret

    def dist_n_tuple(self, text:str, laenge:int) -> Set[Tuple[str, int]]:
        """Überprüft alle Teilstrings aus text mit der gegebenen laenge und liefert ein Set
        mit den Abständen aller Wiederholungen der Teilstrings in text.
        Usage examples:
        >>> k = Kasiski()
        >>> k.dist_n_tuple("heissajuchei", 2) == {('ei', 9), ('he', 9)}
        True
        >>> k.dist_n_tuple("heissajuchei", 3) == {('hei', 9)}
        True
        >>> k.dist_n_tuple("heissajuchei", 4) == set()
        True
        >>> k.dist_n_tuple("heissajucheieinei", 2) == \
        {('ei', 5), ('ei', 14), ('ei', 3), ('ei', 9), ('ei', 11), ('he', 9), ('ei', 2)}
        True
        """

        ret: Set[Tuple[str, int]] = set()

        for i in range (0, len(text)-(laenge-1)):
            sub_text = text[i:i+laenge]

            if len(self.allpos(text, sub_text)) >= 2:
                all_dist = self.alldist(text, sub_text)
                for j in all_dist:
                    ret.add((sub_text, j))

        return ret




