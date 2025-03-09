__author__ = "Danijel Stamenkovic"

import ipaddress
import subprocess

"""
Diese Methode liest eine Netzadresse mit Suffix ein und pingt anschließend
alle gültigen Host-Adressen des gesamten Subnetzes. Das Ganze geschieht
ohne Multithreading, also alle Pings werden der Reihe nach ausgefürt.
"""


def main():
    network = input("Geben Sie das Netzwerk an (in der Form X.X.X.X/X): ")

    try:
        net = ipaddress.ip_network(network)

        for host in net.hosts():
            subprocess.run(["ping", str(host)], creationflags=subprocess.CREATE_NEW_CONSOLE)

    except ValueError as e:
        print(f"Fehler: {e}")

if __name__ == "__main__":
    main()