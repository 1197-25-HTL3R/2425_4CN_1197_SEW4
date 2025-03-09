__author__ = 'Danijel Stamenkovic'

import re
import shutil
from pathlib import Path

"""
Kopiert alle Dateien mit der Extension .jpg aus dem Ordner SourcePath
in den Ordner DestinationPath, wobei die Dateien in Unterordner, die 
nach ihren Zeitstempeln geordnet sind, gespeichert werden.
"""

def main():
    sourcepath = input("Source Path: ")
    destinationpath = input("Destination Path: ")

    sourcepath = Path(sourcepath)
    destinationpath = Path(destinationpath)

    regex = re.compile("(\d{4})(\d{2})(\d{2})_")

    for image in sourcepath.iterdir():
        if image.suffix.lower() == ".jpg" and image.is_file():
            matches = regex.match(image.stem)
            if matches:
                year, month, day = matches.groups()

                folderpath = destinationpath.joinpath(year, month, day)
                folderpath.mkdir(parents=True, exist_ok=True)
                filepath = folderpath.joinpath(image.name)

                shutil.copy(image, filepath)

                print(f"Kopiert: {image} -> {filepath}")
            else:
                print(f"Übersprungen, kein gültiger Zeitstempel: {image.name} -> {image.name}")
        else:
            print(f"Übersprungen, falsche Extension: {image.name}")

if __name__ == "__main__":
    main()