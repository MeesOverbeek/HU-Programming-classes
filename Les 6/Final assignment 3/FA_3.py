def toon_aantal_kluizen_vrij():
    lst = []
    inhoud = open('kluizen.txt')
    reader = inhoud.readlines()
    for x in reader:
        if x != '\n':
            lst.append(x.strip().split(';'))
    vrij = 12 - len(lst)
    print('Er zijn ' + str(vrij) + ' kluisjes vrij')

    vol = []
    kluisnummers = []
    for x in lst:
        kluisnummers.append(int(x[0]))
    for x in kluisnummers:
        if x in kluisnummers:
            vol.append(x)
    print("De kluisjes/het kluisje- " + str(vol).strip("[").strip("]") + " -is/zijn bezet.\n")


def nieuwe_kluis():
    lst = []
    kluisnummers = []
    vol =[]
    content = open('kluizen.txt','r')
    reader = content.readlines()
    for x in reader:
        if x != '\n':
            lst.append(x.strip().split(';'))
    for x in lst:
        kluisnummers.append((int(x[0])))
    for x in kluisnummers:
        if x in kluisnummers:
            vol.append(x)
    print("De kluisjes " + str(vol).strip("[").strip("]") + " zijn bezet.")
    content.close()
    nummer = int(input('Voer een kluisnummer in '))
    if len(kluisnummers) == 12:
        print('Er zijn geen kluisjes meer vrij\n')
        nieuwe_kluis()
    elif nummer in kluisnummers:
        print('Dat kluisje is bezet\n')
        nieuwe_kluis()
    elif nummer not in kluisnummers and nummer <13 and nummer > 0:
        code = input('Voer een kluiscode in ')
        content = open('kluizen.txt','a')
        content.write(str('\n')+'{};{}'.format(nummer, code))
        print('U heeft kluisje ' + str(nummer)+' gekregen\n')
    elif nummer > 12:
        print('Er zijn maar 12 kluisjes\n')
        nieuwe_kluis()
    elif nummer < 0:
        print('U kunt geen negatieve kluisjes opgegven\n')


def kluis_openen():
    lst = []
    nummer = input('Voer een kluisnummer in ')
    code = input('Voer uw code in ')
    content = open('kluizen.txt')
    reader = content.readlines()
    content.close()
    for x in reader:
        lst.append(x.strip().split(';'))
    for x in lst:
        if nummer == x[0] and code == x[1] and 12 >= int(nummer):
            stop = print('U kunt het kluisje openen\n')
            return stop
        elif int(nummer) > 12:
            print('Er zijn maar 12 kluisjes')
            break
    else:
        print('Wachtwoord en kluisnummer komen niet overeen\n')


while True:
    print('1: Ik wil weten hoeveel kluizen nog vrij zijn\n2: Ik wil een nieuwe kluis\n3: Ik wil toegang tot mijn klas\n4: Sluit af')
    user = input('Maak uw keuze ')
    if user == '1':
        toon_aantal_kluizen_vrij()
    elif user == '2':
        nieuwe_kluis()
    elif user == '3':
        kluis_openen()
    elif user == '4':
        break
    else:
        print('U kunt maar tussen 1 tot en met 4 kiezen\n')
