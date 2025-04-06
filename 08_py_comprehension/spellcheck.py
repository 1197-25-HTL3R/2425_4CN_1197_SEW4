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

    Beispiel:
    >>> #Angenommen, 'de-en.txt' enthält:
    >>> #Hallo
    >>> #Welt
    >>> #Python
    >>> read_all_words("de-en.txt")
    {'hallo', 'welt', 'python'}
    """

    with open(filename, mode = "r", encoding = "utf-8") as file:
        return {line.strip() for line in file if line.strip()}
