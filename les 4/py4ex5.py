def kwadraten_som(grondGetallen):
    totaalSom = int()
    for getal in grondGetallen:
        if getal > 1:
            totaalSom += getal**2
    return totaalSom

print(kwadraten_som([4, 5, 3, -81]))