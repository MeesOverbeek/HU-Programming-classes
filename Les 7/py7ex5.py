names = {}

while True:
    nameInput = str(input('Volgende naam: '))
    if nameInput == '':
        for name in names:
            print('Er is/zijn {} student(en) met de naam {}'.format(names[name], name))
        break
    elif nameInput in names:
        names[nameInput] += 1
    else:
        names[nameInput] = 1