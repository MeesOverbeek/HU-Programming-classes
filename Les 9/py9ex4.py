import csv
with open('producten.csv', 'r', newline='\n') as myFile:
    reader = csv.reader(myFile,delimiter=';')
    for x in reader:
        if 'artikelnummer' not in x:
            print('x')
            break


bestand = 'producten.csv'
while True:
    eind = input('Wilt u stoppen?: ')
    if eind == 'nee':
        artikelnummer = input('Voer artikelnummer in: ')
        artikelcode = input('Voer artikelcode in: ')
        naam = input('voer naam in: ')
        vooraad = input('Voer voorraadnummer in: ')
        prijs = input('Voer prijs in: ')
        reader = open(bestand, 'a', newline='\n')
        writer = csv.writer(reader, delimiter=';')
        writer.writerow((artikelnummer, artikelcode, naam, vooraad, prijs))
        reader.close()
    elif eind == 'ja':
        break
    else:
        print('Kies uit nee of ja: ')

with open('producten.csv', 'r') as fileCsv:
    reader = csv.reader(fileCsv, delimiter=';')
    for x in reader:
        print(x)