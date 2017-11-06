def calculate():
    zin = input('Voer een zin in: ')
    lijst = []
    woorden = []
    nummer = []
    lijst.append(zin)
    for woord in lijst:
        woorden.append((woord.split(' ')))
    for woord in woorden:
        for q in woord:
            nummer.append(len (q))
    gem = int(sum(nummer)/len(nummer))
    print('de gemmidelde lengte van de woorden in de zin is ' + str(gem))
calculate()