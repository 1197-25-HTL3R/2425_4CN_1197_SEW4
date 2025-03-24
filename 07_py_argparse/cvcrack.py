__author__ = "Danijel Stamenkovic"

import argparse
import sys

import kasisky
from kasisky import Kasiski

"""
cvcrypt.py – Caesar & Vigenere En-/Decrypter by STA / HTL Rennweg

Usage:
    python cvcrypt.py [options] infile outfile

Options:
    -h, --help            Zeigt diese Hilfe an und beendet das Programm.
    -c {caesar,c,vigenere,v}, --cipher {caesar,c,vigenere,v}
                          Zu verwendende Chiffre (Standard: caesar).
    -v, --verbose         Detaillierte Ausgaben (z.B. "Encrypting ...").
    -q, --quiet           Nur minimale Ausgabe.
    -d, --decrypt         Entschlüsseln.
    -e, --encrypt         Verschlüsseln.
    -k KEY, --key KEY     Verschlüsselungs-/Entschlüsselungsschlüssel.
"""

parser = argparse.ArgumentParser(description="cvcrack - Caesar & Vigenere key cracker by PAC / HTL Rennweg")
parser.add_argument("infile", help="The path of the input file", type=str)
parser.add_argument("-c","--cipher", help="The used encryption", choices=["caesar","c","vigenere","v"])

group_v_q = parser.add_mutually_exclusive_group()
group_v_q.add_argument("-v","--verbose", help="Shows detailed information", action="store_true")
group_v_q.add_argument("-q","--quiet", help="Returns only key", action="store_true")

args = parser.parse_args()

try:
    input_file = open(args.infile).read()
except IsADirectoryError:
    print("The input file does not exist")
    sys.exit(1)
except PermissionError:
    print("Permission denied")
    sys.exit(1)
except FileNotFoundError:
    print("The input file does not exist")
    sys.exit(1)
except Exception:
    print("Unexpected error:", sys.exc_info()[0])
    sys.exit(1)

if args.cipher == "caesar" or args.cipher == "c":
    key = kasisky.Caesar.crack(input_file)[0]
else:
    key = Kasiski(input_file).crack_key(5)[0]

if args.verbose:
    print(f'Cracking {("Vigenere" if args.cipher == "vigenere" or args.cipher == "v" else "Caesar")}-encrypted file {args.infile}: Key = {key}')
else:
    print(key)