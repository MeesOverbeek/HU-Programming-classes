def counting(file):
    Inhoud = open(file, 'r')
    reader = Inhoud.read()
    print('Deze file heeft '+str(reader.count('\n')+1)+ ' regels')
    Inhoud.close()
    Inhoud = open(file, 'r')
    Lijst = []
    numbers = []
    reader = Inhoud.readlines()
    for nummer in reader:
        Lijst.append(nummer.strip().split(','))
    for nummer in Lijst:
        numbers.append(nummer[0])
    maximumNumber= max(numbers)
    lineNumber = numbers.index(max(numbers))+1
    print('Het grootste kaartnummer is ' + str(maximumNumber) + ' op regel ' + str(lineNumber))
counting('kaartnummer.txt')
