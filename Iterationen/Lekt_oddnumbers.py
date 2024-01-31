i = 10003
anzahlungerade = 0

while True:

    if i % 2 != 0:
        anzahlungerade += 1
        print(i)
    i += 1

    if anzahlungerade == 10:
        break