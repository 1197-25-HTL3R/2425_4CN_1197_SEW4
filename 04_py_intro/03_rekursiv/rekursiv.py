from time import time


def M(n) -> int:
    """
    Diese Funktion implementiert den rekursiven McCarthy-91-Algorithmus.
    Für Eingaben größer als 100 wird 10 subtrahiert.
    Für Eingaben kleiner oder gleich 100 erfolgt eine doppelte rekursive Verarbeitung, bis das Ergebnis nach den Regeln berechnet ist.

    :param n: Ganzzahlige Eingabe.
    :type n: int
    :return: Das berechnete Ergebnis der McCarthy-91-Funktion.
    :rtype: int
    """

    if n == 0:
        return 0

    if n > 100:
        return n - 10
    else:
        return n + M(M(n + 11))


if __name__ == "__main__":
    t0 = time()

    m_list = [M(n) for n in range(200)]
    print("m_list:", m_list)

    m_dict = {n: M(n) for n in range(200)}
    print("m_dict:", m_dict)

    duration = time() - t0
    print(f"Berechnungsdauer: {duration:.4} Sekunden")
