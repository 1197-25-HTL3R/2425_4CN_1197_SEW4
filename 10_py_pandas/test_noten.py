import pandas as pd
from noten import read_xml, read_csv, merge_dataframes, filter_faecher

def test_read_xml():
    df = read_xml("tests/schueler_test.xml")
    assert "Nummer" in df.columns
    assert "Vorname" in df.columns

def test_read_csv():
    df = read_csv("tests/noten_test.csv")
    assert "Nummer" in df.columns
    assert "Gegenstand" in df.columns

def test_merge():
    schueler = pd.DataFrame({"Nummer": ["1"], "Vorname": ["Test"], "Nachname": ["Schueler"]})
    noten = pd.DataFrame({"Nummer": ["1"], "Gegenstand": ["SEW"], "Note": ["1"]})
    merged = merge_dataframes(schueler, noten, "Nummer")
    assert merged.shape[0] == 1

def test_filter_faecher():
    df = pd.DataFrame({
        "Nummer": ["1", "1"],
        "Gegenstand": ["SEW", "ITP"],
        "Note": ["1", "2"]
    })
    filtered = filter_faecher(df, "SEW")
    assert filtered.shape[0] == 1
    filtered2 = filter_faecher(df, "SEW,ITP")
    assert "Schnitt" in filtered2.columns

print("Alle Tests bestanden!")
