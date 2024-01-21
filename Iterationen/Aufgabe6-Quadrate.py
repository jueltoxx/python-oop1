start = int(input("Startzahl: "))
end = int(input("Endzahl: "))

end += 1

range = range(start,end)

for n in range:
    value = n * n
    print(n, value)