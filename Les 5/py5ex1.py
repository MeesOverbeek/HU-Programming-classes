def convert(temparatuur):
    return temparatuur * 1.8 + 32

def tabel():
    print('  F\t\t\tC')
    for temp in range(-30, 41, 10):
        Farenheit = convert(temp)
        print('{:3}{:11}'.format(temp,Farenheit))
tabel()