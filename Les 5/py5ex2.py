infile = open('kaartnummer.txt')
lijst = []
inhoud = infile.readlines()
for naam in inhoud:
    lijst.append(naam.split(','))

infile.close()
for naam in lijst:
    print(naam[1].strip() + 'heeft kaartnummer: ' + naam[0])