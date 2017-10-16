CijferICOR = 8
CijferPROG = 7
CijferCSN = 6

Gemiddelde = (CijferCSN + CijferICOR + CijferPROG) / 3
Beloning = (Gemiddelde * 30.0)

Overzicht = 'mijn cijfers (gemiddeld een ' + str(Gemiddelde) + ') levert een beloning van €' + str(Beloning) + ' op!'

print(Overzicht)