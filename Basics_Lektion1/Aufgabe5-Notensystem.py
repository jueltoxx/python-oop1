pkt = input("Geben Sie Ihre Punktzahl ein: ")
pkt = int(pkt)

if pkt < 25:
    print("F")
elif 25 <= pkt < 45:
    print("E")
elif pkt >= 45 and pkt < 50:
    print("D")
elif pkt >= 50 and pkt < 60:
    print("C")
elif pkt >= 60 and pkt < 80:
    print("B")
else:
    print("A")