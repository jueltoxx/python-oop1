def entferne_duplikate(liste):
    # Verwende ein Set, um Duplikate zu entfernen
    return list(set(liste))

# Beispielliste mit Duplikaten
beispiel_liste = [1, 2, 3, 4, 2, 3, 5, 6, 1]

# Duplikate entfernen und das Ergebnis ausgeben
print("Liste vor dem Entfernen von Duplikaten:", beispiel_liste)
ergebnis_liste = entferne_duplikate(beispiel_liste)
print("Liste nach dem Entfernen von Duplikaten:", ergebnis_liste)
