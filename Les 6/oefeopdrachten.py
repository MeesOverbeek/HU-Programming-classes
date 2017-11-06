#def BMI(weight, height):
#   'functie print het BMI report'
#
#   bmi = (int(weight) * 703) / (int(height) ** 2)
#
#    if bmi < 18.5:
#        print('you are underweight')
#    elif bmi < 25:
#        print('you are of healthy weight')
#    else:
#        print('you are overweight')

#hoogte = input('geef hier je gewicht: ')
#gewicht = input('geef hier je lengte: ')

#BMI(gewicht, hoogte)

#def acronym(phrase):
#    'de functie geeft het acroniem terug'

#    'split zin naar een lijst van woorden'
#    words = phrase.split()

#    'verzamel alle eerste letters als hoofdletter van elk woord'
#    resultaat = ''
#    for w in words:
#        resultaat = resultaat + w[0].upper()
#    return resultaat

#phrase = input('geef hier je zin: ')
#print(acronym(phrase))

#def nested(n):
#    for j in range(n):
#        for i in range(n):
#            print(i, end=' ')
#        print()
#
#j = int(input('geef hier je cijfer: '))
#nested(j)
#
#def nested2(n):
#    for j in range(n):
#        for i in range(j+1):
#            print(i, end=' ')
#        print()
#
#nested2(j)