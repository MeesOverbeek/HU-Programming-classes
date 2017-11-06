import csv

csvFilePad = 'scores.csv'

BestaandCsvBestand = open(csvFilePad, 'r')
csvFile = csv.reader(BestaandCsvBestand, delimiter=';')

csvBestandRijen = list()
highestScore = int()
highestScoreIndex = int()

for index, row in enumerate(csvFile):
    csvBestandRijen.append(row)
    if int(row[2]) > highestScore:
        highestScore = int(row[2])
        highestScoreIndex = index

print('De hoogste score is: {} op {} behaald door {}'.format(csvBestandRijen[highestScoreIndex][2], csvBestandRijen[highestScoreIndex][1], csvBestandRijen[highestScoreIndex][0]))
