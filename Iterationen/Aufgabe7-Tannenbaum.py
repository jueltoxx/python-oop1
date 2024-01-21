def sterne(anzahlsterne):
    sterne = range(0,anzahlsterne)
    for n in sterne:
        print("* ", end="")

def leerschlaege(anzahls):
    leerschlaege = range(0,anzahls)
    for n in leerschlaege:
        print(" ", end="")


def printatree(anzahllinien):
    linien = range(1,anzahllinien)
    for n in linien:
        anzsterne = 2 * (n-1) + 1
        schlaege = linien.stop * 2 - n*2
        leerschlaege(schlaege)
        sterne(anzsterne)
        print("")


hoehe = int(input("Geben Sie die Höhe des Baumes ein: "))
hoehe += 1
printatree(hoehe)
