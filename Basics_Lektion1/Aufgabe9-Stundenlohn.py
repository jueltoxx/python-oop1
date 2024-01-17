stundenlohn = int(input("Stundenlohn: "))
arbeitsstunden = float(input("Arbeitsstunden: "))
wochentag = input("Wochentag: ")

multiplikator = 1

if wochentag.lower() == "sonntag":
    multiplikator = 2

def tageslohnrechner(stundenlohn,arbeitsstunden,multiplikator):
    tageslohn = stundenlohn * arbeitsstunden * multiplikator
    return tageslohn

todayspay = tageslohnrechner(stundenlohn,arbeitsstunden,multiplikator)

print(todayspay)