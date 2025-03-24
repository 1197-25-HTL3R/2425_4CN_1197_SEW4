__author__ = "Danijel Stamenkovic"
import argparse
import sys

import kasisky

"""
cvcrack.py – Caesar & Vigenere key cracker by STA / HTL Rennweg

Usage:
    python cvcrack.py [options] infile

Options:
    -h, --help            Zeigt diese Hilfe an und beendet das Programm.
    -c {caesar,c,vigenere,v}, --cipher {caesar,c,vigenere,v}
                          Zu verwendende Chiffre (Standard: caesar).
    -v, --verbose         Detaillierte Ausgabe.
    -q, --quiet           Nur den wahrscheinlichsten Key ausgeben.
"""

parser = argparse.ArgumentParser(description="Kasiski Argparser by STA / HTL Rennweg")
parser.add_argument("infile", help="The path of the input file", type=str)
parser.add_argument("outfile", help="The path of the output file", type=str)

group_v_q = parser.add_mutually_exclusive_group()
group_v_q.add_argument("-v", "--verbose", action="store_true")
group_v_q.add_argument("-q", "--quiet", action="store_true")

group_d_e = parser.add_mutually_exclusive_group()
group_d_e.add_argument("-d", "--decrypt", action="store_true")
group_d_e.add_argument("-e", "--encrypt", action="store_true")

parser.add_argument("-c","--cipher", help="The used encryption", choices=["caesar","c","vigenere","v"])
parser.add_argument("-k","--key", help="The used encryption key")

args = parser.parse_args()

if args.key:
    key = args.key
else:
    print("No key argument used", file=sys.stderr)
    exit(1)

try:
    input_file = open(args.infile).read()
except FileNotFoundError:
    print(args.infile + "File not found", file=sys.stderr)
    exit(1)
except PermissionError:
    print(args.infile + "Permission denied", file=sys.stderr)
    exit(1)
except IsADirectoryError:
    print(args.infile + "Directory not found", file=sys.stderr)
    exit(1)
except Exception:
    print(args.infile + "Unexpected error:", sys.exc_info()[0], file=sys.stderr)
    exit(1)




