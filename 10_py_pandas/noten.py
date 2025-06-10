__author__ = "Danijel Stamenkovic"

"""
Hilfsprogramm zum Zusammenführen von Noten- und Schülerlisten.
"""

import sys
import os
import argparse
import pandas as pd
import re

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

def read_xml(filename: str) -> pd.DataFrame:
    """
    Liest Schülerdaten aus einer XML-Datei mit Regex aus und gibt einen DataFrame zurück.
    Erwartete Felder: Nummer, Anrede, Vorname, Nachname, Geburtsdatum
    """
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(
        r"<Schueler>\s*<Nummer>(\d+)</Nummer>\s*<Anrede>([^<]+)</Anrede>\s*<Vorname>([^<]+)</Vorname>\s*<Nachname>([^<]+)</Nachname>\s*<Geburtsdatum>([^<]+)</Geburtsdatum>\s*</Schueler>",
        re.DOTALL
    )
    result = re.findall(pattern, content)
    df = pd.DataFrame(result, columns=["Nummer", "Anrede", "Vorname", "Nachname", "Geburtsdatum"], dtype=str)
    return df

def read_csv(filename: str) -> pd.DataFrame:
    """
    Liest eine CSV-Datei mit Noten ein und gibt einen DataFrame zurück.
    """
    return pd.read_csv(filename, dtype=str)

def merge_dataframes(
    df1: pd.DataFrame,
    df2: pd.DataFrame,
    key: str
) -> pd.DataFrame:
    """
    Verknüpft zwei DataFrames über die angegebene Schlüsselsäule.
    """
    if key not in df1.columns or key not in df2.columns:
        print(f"Fehler: Spalte '{key}' zum Verknüpfen nicht gefunden.", file=sys.stderr)
        sys.exit(3)
    merged = pd.merge(df1, df2, on=key, how="inner")
    return merged

if __name__ == "__main__":
    args = parse_args()
    check_file_exists(args.n)
    check_file_exists(args.s)
    schueler_df = read_xml(args.s)
    noten_df = read_csv(args.n)
    merged_df = merge_dataframes(schueler_df, noten_df, args.m)


