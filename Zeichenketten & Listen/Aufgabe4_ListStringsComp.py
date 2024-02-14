liste = ["mein penis ist geil","mien penis ist steil","Fick dich du hurensohn","Ferdammtnochmal deine Hurentochter hat meine Katze gefickt!"]
def aehnliche_zeichenketten_anzahl(liste):
    anzahl = 0
    for wort in liste:
        if len(wort) >= 2 and wort[0] == wort[-1]:
            anzahl += 1
    return anzahl

# Beispielliste von Zeichenketten
beispiel_liste = ["anna", "hallo", "elefant", "level", "renner", "python", "otto"]

# Die Anzahl der ähnlichen Zeichenketten in der Liste ermitteln und ausgeben
print("Die Anzahl der ähnlichen Zeichenketten in der Liste beträgt:", aehnliche_zeichenketten_anzahl(liste))
