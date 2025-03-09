__author__ = 'Danijel Stamenkovic'

"""
Das Programm liest über die Tastatur einen Pfad und eine Da-
teinamenserweiterung ein und durchsucht rekursiv nach allen Dateien mit dieser Extension und gibt alle
gefundenen Dateien mit ihrem absoluten Pfad aus.
"""

from pathlib import Path


def main():
    base_path = input("Geben Sie den Pfad ein: ")
    extension = input("Geben Sie die Extension ein: ")

    path = Path(base_path)

    print([path.name for path in sorted(path.rglob("*."+extension))])

if __name__ == "__main__":
    main()