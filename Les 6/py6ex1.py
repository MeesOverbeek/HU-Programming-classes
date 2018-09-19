def seizoen(maand):
    if maand == 12:
        print('Winter')
    elif 11 > maand > 8:
        print('Herfst')
    elif 8 > maand > 5:
        print('Zomer')
    elif 5 > maand > 2:
        print('Lente')
    else:
        print('Winter')

seizoen(9)