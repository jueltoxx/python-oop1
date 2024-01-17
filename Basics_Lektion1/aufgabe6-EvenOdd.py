def check(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")

nummer = input("Geben Sie eine Zahl ein: ")
nummer = int(nummer)
check(nummer)