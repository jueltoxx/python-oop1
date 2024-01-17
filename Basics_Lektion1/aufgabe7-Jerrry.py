preis = 5.90

name = input("Geben Sie Ihren Namen ein: ")

if name.lower() == "Jerry":
    print("Hi Jerry")
else:
    print("Hallo ",name)
    portionen = input("Geben Sie die Anzahl Portionen ein: ")
    portionen = int(portionen)
    totalpreis = portionen * preis
    print(totalpreis)