user = input('Geef een string van vier letters: ')
while True:
    if len(user)==4:
        print(str(user) + ' is geslaagd')
        break
    else:
        user = input('Geef een string van vier letters: ')