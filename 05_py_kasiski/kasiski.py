import collections
import itertools
from collections.abc import Collection
from typing import List, Set, Tuple, Counter


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

        >>> str = 'Vor einem großen Walde wohnte ein armer Holzhacker mit seiner Frau und seinen zwei Kindern; das Bübchen hieß Hänsel und das Mädchen Gretel. Er hatte wenig zu beißen und zu brechen, und einmal, als große Teuerung ins Land kam, konnte er das tägliche Brot nicht mehr schaffen. Wie er sich nun abends im Bette Gedanken machte und sich vor Sorgen herumwälzte, seufzte er und sprach zu seiner Frau: "Was soll aus uns werden? Wie können wir unsere armen Kinder ernähren da wir für uns selbst nichts mehr haben?'
        >>> caesar = Caesar()
        >>> caesar.crack(str)
        ['a']
        >>> caesar.crack(str, 100) # can't be more than 26
        ['a', 'n', 'j', 'w', 'e', 'r', 'z', 'o', 'k', 'b', 'm', 'q', 'l', 'v', 'p', 'f', 'h', 'u', 's', 't', 'x', 'd', 'i', 'y', 'g', 'c']
        >>> crypted = caesar.encrypt(str, "y")
        >>> caesar.crack(crypted, 3)
        ['y', 'l', 'h']
        """

        crypttext = Caesar.to_lowercase_letter_only(crypttext)

        letters = {
            'e': 17.40, 'n': 9.78, 'i': 7.55, 's': 7.27, 'r': 7.00,
            'a': 6.51, 't': 6.15, 'd': 5.08, 'h': 4.76, 'u': 4.35,
            'l': 3.44, 'c': 3.06, 'g': 3.01, 'm': 2.53, 'o': 2.51,
            'b': 1.89, 'w': 1.89, 'f': 1.66, 'k': 1.21, 'z': 1.13,
            'p': 0.79, 'v': 0.79, 'j': 0.27, 'y': 0.04, 'x': 0.03,
            'q': 0.02
        }

        distances: dict[str, int] = {char: 0 for char in 'abcdefghijklmnopqrstuvwxyz'}

        for key in range(0, 26):
            for char in range(0, 26):
                keys_frequency = Caesar.decrypt(crypttext, chr(key + ord('a'))).count(chr(char + ord('a'))) / len(
                    crypttext) * 100
                distances[chr(key + ord('a'))] += ((keys_frequency - letters[chr(char + ord('a'))]) ** 2)

        ret = sorted(distances.items(), key=lambda item: item[1])

        return [kv[0] for kv in ret[:elements]]

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

    def alldist(self, text: str, teilstring: str) -> Set[int]:
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
                ret.add(abs(next(num) - i))
                cycle_end -= 1

        ret = {x for x in ret if x != 0}

        return ret

    def dist_n_tuple(self, text: str, laenge: int) -> Set[Tuple[str, int]]:
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

        for i in range(0, len(text) - (laenge - 1)):
            sub_text = text[i:i + laenge]

            if len(self.allpos(text, sub_text)) >= 2:
                all_dist = self.alldist(text, sub_text)
                for j in all_dist:
                    ret.add((sub_text, j))

        return ret

    def dist_n_list(self, text: str, laenge: int) -> List[int]:
        """Wie dist_tuple, liefert aber nur eine aufsteigend sortierte Liste der
        Abstände ohne den Text zurück. In der Liste soll kein Element mehrfach vorkommen.
        Usage examples:
        >>> k = Kasiski()
        >>> k.dist_n_list("heissajucheieinei", 2)
        [2, 3, 5, 9, 11, 14]
        >>> k.dist_n_list("heissajucheieinei", 3)
        [9]
        >>> k.dist_n_list("heissajucheieinei", 4)
        []"""

        ret = set()

        tuple_set = self.dist_n_tuple(text, laenge)
        for (i, j) in tuple_set:
            ret.add(j)

        return sorted(ret)

    @staticmethod
    def ggt(x: int, y: int) -> int:
        """Ermittelt den größten gemeinsamen Teiler von x und y.
        Usage examples:
        >>> k = Kasiski()
        >>> k.ggt(10, 25)
        5
        >>> k.ggt(10, 25)
        5"""

        while y:
            x, y = y, x % y
        return x

    def ggt_count(self, zahlen: List[int]) -> Counter:
        """Bestimmt die Häufigkeit der paarweisen ggt aller Zahlen aus list.
        Usage examples:
        >>> k = Kasiski()
        >>> k.ggt_count([12, 14, 16])
        Counter({2: 2, 12: 1, 4: 1, 14: 1, 16: 1})
        >>> k.ggt_count([10, 25, 50, 100])
        Counter({10: 3, 25: 3, 50: 2, 5: 1, 100: 1})
        """

        ggt_list = []

        for i in range(len(zahlen)):
            for j in range(i, len(zahlen)):
                ggt_list.append(self.ggt(zahlen[i], zahlen[j]))

        ret: Counter[int] = collections.Counter(ggt_list)

        return ret

    @staticmethod
    def get_nth_letter(s: str, start_int, n: int) -> str:
        """Extrahiert aus s jeden n. Buchstaben beginnend mit index start.
        Usage examples:
        >>> k = Kasiski()
        >>> k.get_nth_letter("Das ist kein kreativer Text.", 1, 4)
        'asektrx'"""

        ret = ""

        for c in range(start_int, len(s)):
            if (c - start_int) % n == 0:
                ret += s[c]

        return ret

    def crack_key(self, length: int) -> str:
        """
        >>> sample = "diesisteineinfacherlangerbeispieltextgdrgdgrdhddiesisteineinfacherlangerbeispieltextfeqgwgwgdiesisteineinfacherlangerbeispieltext"
        >>> encrypted = Vigenere.cncrypt(sample, "apfel")
        >>> k = Kasiski(encrypted)
        >>> k.crack_key(3)
        'apfel'
        """

        distances = self.dist_n_list(self.crypttext, length)
        key_length = self.ggt_count(distances).most_common(1)[0][0]
        key_ret = ""

        for i in range(key_length):
            text = self.get_nth_letter(self.crypttext, i, key_length)
            key_ret += Caesar.crack(text, 1)[0]

        return key_ret


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    example_text = (
        "Es war einmal in einem alten, ehrwürdigen Land, "
        "wo die Worte der Dichter und Denker wie kostbare Juwelen behandelt wurden. "
        "In den langen, ehrfurchtgebietenden Zeilen eines Werkes, das aus den Archiven von Projekt Gutenberg stammt, "
        "verbirgt sich Weisheit und Schönheit, die den Geist beflügeln und die Seele berühren."
    )

    key = "apfel"

    encrypted = Vigenere.cncrypt(example_text, key)
    print("Verschlüsselter Text:")
    print(encrypted)
    print("\n" + "-" * 60 + "\n")

    k = Kasiski(encrypted)
    deciphered_key = k.crack_key(3)
    print("Gefundener Schlüssel:", deciphered_key)
    print("\n" + "-" * 60 + "\n")

    # Entschlüsseln mit dem gefundenen Schlüssel
    decrypted = Vigenere.decrypt(encrypted, deciphered_key)
    print("Entschlüsselter Text:")
    print(decrypted)
