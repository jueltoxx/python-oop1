#Funktionen

#Summieren
def sum(x,y):
    result=x+y
    return result

#Subtrahieren
def sub(x,y):
    result=x-y
    return result

#Dividieren
def div(x,y):
    result=x/y
    return result

#Multiplizieren
def mpk(x,y):
    result=x*y
    return result

#User Inputs
operation = input("Geben Sie eine Operation ein [Addieren, Subtrahieren, Multiplizieren, Dividieren] : ")
zahl1 = int(input("Geben Sie Zahl1 ein: "))
zahl2 = int(input("Geben Sie die Zahl 2 ein: "))

#work
if operation.lower() == "addieren" or operation.lower() == "+":
    resultat = sum(zahl1,zahl2)
    print("Das Ergebnis von",zahl1,"+",zahl2,"ist: ",resultat)
elif operation.lower() == "subtrahieren" or operation.lower() == "-":
    resultat = sub(zahl1,zahl2)
    print("Das Ergebnis von",zahl1,"-",zahl2,"ist: ",resultat)
elif operation.lower() == "dividieren" or operation.lower() == ":":
    resultat = div(zahl1,zahl2)
    print("Das Ergebnis von",zahl1,"/",zahl2,"ist: ",resultat)
elif operation.lower() == "multiplizieren" or operation.lower() == "*":
    resultat = mpk(zahl1,zahl2)
    print("Das Ergebnis von",zahl1,"*",zahl2,"ist: ",resultat)
else:
    print("Es wurde keine passende Operation angegeben.")




