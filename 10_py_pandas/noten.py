__author__ = "Danijel Stamenkovic"

"""
Hilfsprogramm zum Zusammenführen von Noten- und Schülerlisten.
"""

import sys
import os
import argparse

def parse_args():
    """
    Parsed die Kommandozeilenargumente.
    """
    parser = argparse.ArgumentParser(
        description='noten.py by [DEIN NAME] / HTL Rennweg'
    )
    parser.add_argument('-n', metavar='N', help='csv-Datei mit den Noten')
    parser.add_argument('-s', metavar='S', help='xml-Datei mit den Schülerdaten')
    parser.add_argument('-m', metavar='M', default='Nummer', help='Name der Spalte, die zu verknüpfen ist (default = Nummer)')
    parser.add_argument('-f', metavar='F', help='Name der zu filternden Gegenstände (z.B. SEW,ITP)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Gibt die Daten auf der Kommandozeile aus')
    parser.add_argument('-q', '--quiet', action='store_true', help='Keine Textausgabe')
    parser.add_argument('outfile', help='Ausgabedatei (z.B. result.csv)')
    return parser.parse_args()

def check_file_exists(filename: str) -> None:
    """
    Prüft, ob eine Datei existiert, sonst Fehlermeldung auf stderr und exit.
    """
    if filename and not os.path.isfile(filename):
        print(f"Fehler: Datei '{filename}' nicht gefunden.", file=sys.stderr)
        sys.exit(2)

if __name__ == "__main__":
    args = parse_args()
    check_file_exists(args.n)
    check_file_exists(args.s)
