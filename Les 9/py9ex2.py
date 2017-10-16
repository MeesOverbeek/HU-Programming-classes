import datetime
import csv

bestand = 'inloggers.csv'

while True:
    naam = input("Wat is je achternaam?: ")
    if naam != 'einde':
        voorl = input("Wat zijn je voorletters?: ")
        gbdatum = input("Wat is je geboortedatum?: ")
        email = input("Wat is je e-mail adres?: ")
        with open(bestand, 'a', newline='\n') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            vandaag = datetime.datetime.today().strftime('%a %d %B %Y at %H %M')
            writer.writerow((vandaag, voorl, naam, gbdatum, email))
        print('Ingevoerd...\n')
    else:
        print('Afsluiten...')
        break