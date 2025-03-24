__author__ = "Danijel Stamenkovic"
import argparse
import kasisky

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

