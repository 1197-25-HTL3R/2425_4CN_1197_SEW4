__author__ = "Danijel Stamenkovic"

from typing import List, Tuple


def read_all_words(filename: str) -> set[str]:
    """
    Liest alle Wörter aus der angegebenen Datei ein und gibt sie als Menge zurück.

    Es wird davon ausgegangen, dass jedes Wort in einer eigenen Zeile steht.
    Vor der Aufnahme werden führende und nachgestellte Leerzeichen entfernt.

    Args:
        filename (str): Pfad zur Datei mit den Wörtern.

    Returns:
        set[str]: Eine Menge aller Wörter aus der Datei.
    """

    with open(filename, mode = "r", encoding = "utf-8") as file:
        return {line.strip() for line in file if line.strip()}


def split_word(wort:str) -> List[Tuple[str, str]]:
    """
        Erzeugt eine Liste von Aufteilungen des Wortes, indem jeweils ein Zeichen
        ausgelassen wird. Für jedes Zeichen im Wort wird ein Tupel (head, tail) erzeugt,
        wobei 'head' der Teil vor dem aktuellen Zeichen und 'tail' der Teil nach dem
        aktuellen Zeichen ist.

        Beachte: Für ein Wort der Länge n werden n Tupel erzeugt.

        Beispiele:
        >>> split_word("abc")
        [('', 'abc'), ('a', 'bc'), ('ab', 'c'), ('abc', '')]
        """
    ret: List[Tuple[str, str]] = []

    for i in range(len(wort)+1):
        ret += [(wort[0:i], wort[i:len(wort)])]

    return ret


