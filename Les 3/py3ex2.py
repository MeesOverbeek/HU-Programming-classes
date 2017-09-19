age = eval(input('geef hier je leeftijd: '))
paspoort = input('heb je een Nederlands paspoort?: ')
line = 'U mag stemmen'
if age >= 18 and (paspoort == 'Ja' or paspoort == 'ja'):
    print(line)
