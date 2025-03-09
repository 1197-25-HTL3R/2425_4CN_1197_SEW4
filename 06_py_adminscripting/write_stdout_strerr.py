import sys, time
if __name__ == "__main__":
    print("Dies ist eine Nachricht auf stdout")  # Ausgabe auf stdout
    print("Dies ist eine Nachricht auf stderr", file=sys.stderr)  # Ausgabe auf stderr
    print(f"{sys.argv} wartet zehn Sekunden:")
    time.sleep(10)
    print(f"{sys.argv} wird beendet.")
    sys.exit(42)