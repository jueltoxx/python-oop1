zahlen = [444444,32,1234,243600000,7345,2653,4]

aktuelleZahl=0

for zahl in zahlen:
    if zahl > aktuelleZahl:
        aktuelleZahl = zahl

print(aktuelleZahl)