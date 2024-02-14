zeilen = 5
spalten = 10

for i in range(1,zeilen): # zeilen
    print(i, "" , end="")

    for j in range(i,spalten): # Spalten
        print(j, "" , end="")

    print("z")