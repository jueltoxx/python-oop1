lang = input("Sprache wählen DEU oder ENG: ")

if lang == "ENG":
    x = input("enter number for x: ")
    x = int(x)

    y = input("enter number y:")
    y = int(y)
elif lang == "DEU":
    x = input("Nummer für x eingeben: ")
    x = int(x)

    y = input("Nummer für y eingeben: ")
    y = int(y)

def sum(x,y):
    sum = x + y
    return sum

__hello = ""

summe = sum(x,y)

if summe < 5:
    print("x smaller 5 it equals to", summe)
elif summe == 5:
    print("x equals 5 it equals to", summe)
else:
    print("Sum is larger than 5 it equals to ", summe)
