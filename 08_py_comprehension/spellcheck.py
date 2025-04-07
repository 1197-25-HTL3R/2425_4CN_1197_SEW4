__author__ = "Danijel Stamenkovic"

import string
from typing import List, Tuple, Set


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
    ret = [(wort[:i], wort[i:]) for i in range(len(wort) + 1)]

    return ret

def edit1(wort:str) -> Set[str]:
    """
        Erzeugt alle möglichen Wörter, die durch genau einen Editierfehler (Edit-Distanz 1)
        aus dem gegebenen Wort resultieren. Es werden dabei vier Operationen berücksichtigt:

          - Deletion: Entferne ein Zeichen.
          - Transposition: Vertausche zwei benachbarte Zeichen.
          - Replacement: Ersetze ein Zeichen durch einen anderen.
          - Insertion: Füge ein Zeichen ein.

        Doctest (gekürzt):
        >>> "ac" in edit1("abc") and "acb" in edit1("abc")
        True
        """

    letters = string.ascii_lowercase

    # a)
    delete = {head + tail[1:] for head, tail in split_word(wort) if tail}

    # b)
    swap = {head + tail[1] +  tail[0] + tail[2:] for head, tail in split_word(wort) if len(tail) > 1}

    # c)
    replace = {head + c + tail[1:] for head, tail in split_word(wort) if tail for c in letters if c != tail[0]}

    # d)
    insert = {head + e + tail for head, tail in split_word(wort) if tail for e in letters}

    return delete | swap | replace | insert

def edit1_good(wort:str, alle_woerter:List[str]) -> Set[str]:
    """
      Filtert edit1(wort) und gibt nur Wörter zurück, die im Wörterbuch (alle_woerter) enthalten sind.

      >>> sorted(edit1_good("pyton", ["python", "pylon", "pyton"]))
      ['pylon', 'python']
    """

    dictionary = set(alle_woerter)
    return edit1(wort) & dictionary

def edit2_good(wort:str, alle_woerter:List[str]) -> Set[str]:
    """
        Liefert alle Wörter mit Edit-Distanz 2, die im Wörterbuch (alle_woerter) enthalten sind.

        >>> sorted(edit2_good("pyton", ["python", "pylon", "pyton", "ptyon"]))
        ['ptyon']
    """

    dictionary = set(alle_woerter)
    return {edit2 for edit in edit1(wort) for edit2 in edit1(edit)} & dictionary


