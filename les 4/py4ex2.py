def som(getallenLijst):
    totaal = int()
    for getal in getallenLijst:
        totaal += getal
    return totaal

print(som([7, 3, 6]))