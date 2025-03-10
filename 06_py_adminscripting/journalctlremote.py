__author__ = "Danijel Stamenkovic"

import paramiko
from getpass import getpass

"""
a. Welche Dateien werden erzeugt – wie lautet deren absoluter Pfad?

    Privater Schlüssel: ~/.ssh/id_rsa_junioradmin (oder id_rsa)
    Öffentlicher Schlüssel: ~/.ssh/id_rsa_junioradmin.pub
    Falls Standardpfad: ~/.ssh/id_rsa und ~/.ssh/id_rsa.pub

b. Welche zusätzlichen Informationen werden angezeigt?

    Bestätigung der Schlüsselerstellung
    Speicherort der Schlüssel
    Fingerprint des öffentlichen Schlüssels
    Zufallsbild (Key’s randomart)
    
c. Welche Daten werden kopiert (Quelle – Ziel)?

    Quelle: ~/.ssh/id_rsa_junioradmin.pub (öffentlicher Schlüssel)
    Ziel: ~/.ssh/authorized_keys auf dem Remote-Server

e. Warum darf der private Schlüssel die eigene Maschine NIEMALS verlassen?

    Er ist geheim und dient zur Authentifizierung.
    Falls er gestohlen wird, kann sich jeder ohne Passwort anmelden.

d. Testen: Was passiert jetzt beim Verbinden mit ssh user@IP-Adresse?

    Falls alles richtig eingerichtet ist: Direkte Anmeldung ohne Passwort
    Falls SSH-Schlüssel nicht erkannt wird: Passwort wird weiterhin abgefragt
    
"""

def key_based_connect(host, username, keyfile, passphrase=None):
    print("Connecting to {}...".format(host))
    if not passphrase:
        passphrase = "" #Anstelle von getpass() leere Passphrase benutzt, getpass() geht nicht in der IDE
    pkey = paramiko.RSAKey.from_private_key_file(keyfile, password=passphrase)
    client = paramiko.SSHClient()
    policy = paramiko.AutoAddPolicy()
    client.set_missing_host_key_policy(policy)
    client.connect(host, username=username, pkey=pkey, )
    return client

def main():
    host = "192.168.233.254"
    username = "junioradmin"
    keyfile = "C:/Users/danie/.ssh/id_rsa_junioradmin"
    minutes = input("Eingabe der Zeit in Minuten: ")

    client = key_based_connect(host, username, keyfile)

    stdin, stdout, stderr = client.exec_command(f"journalctl --no-pager --since '{minutes} minutes ago'")
    output = stdout.read().decode("utf-8")
    error = stderr.read().decode("utf-8")

    if output:
        print("Journal Logs:")
        print(output)
    else:
        print("Fehler / Keine Logs gefunden:")
        print(error)

        client.close()


if __name__ == "__main__":
    main()