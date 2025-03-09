__author__ = 'Danijel Stamenkovic'

"""
Ermittelt die Verzeichnisteile eines absoluten Pfads und gibt diese aus.
"""

from pathlib import Path

dateipfad = input("Bitte den absoluten Pfad einer Datei eingeben: ")
p = Path(dateipfad)

print("Dateiname:", p.name)
print("Dateiname ohne Endung (Stem):", p.stem)
print("Dateiendung (Suffix):", p.suffix)
print("Pfad-Anchor:", p.anchor)
print("Verzeichnis, in dem sich die Datei befindet (Parent):", p.parent)

if p.parent == p.parent.parent:
    print("Parent directory does not exist!")
else:
    print("Übergeordnetes Verzeichnis des Ordners:", p.parent.parent)