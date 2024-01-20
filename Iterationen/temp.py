def summe_der_quadrate(start, ende):
    summe = 0
    for zahl in range(start, ende + 1):
        summe += zahl ** 2
    return summe

if __name__ == "__main__":
    start = int(input("Geben Sie den Startwert des Bereichs ein: "))
    ende = int(input("Geben Sie den Endwert des Bereichs ein: "))

    ergebnis = summe_der_quadrate(start, ende)
    print(f"Die Summe der Quadrate im Bereich von {start} bis {ende} beträgt: {ergebnis}")
