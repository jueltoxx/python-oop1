# Beispiel-Liste von Zahlen
numbers = [64, 25, 12, 22, 11, 1, 90]

# Selectionsort-Algorithmus zur Sortierung der Zahlen
n = len(numbers)
# Durchlaufen der Liste
for i in range(n):
    min_index = i
    # Finden des kleinsten Elements im Rest der Listes
    for j in range(i+1, n):
        if numbers[j] < numbers[min_index]:
            min_index = j
    # Vertauschen des aktuellen Elements mit dem kleinsten gefundenen Element
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

# Ausgabe der sortierten Liste
print("Sortierte Liste:")
for num in numbers:
    print(num, end=" ")

