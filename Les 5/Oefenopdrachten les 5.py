lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(lst[ :4])
print(lst[3:6])
print(lst[3:4])
print(lst[-3:-1])
print(lst[3: ])
print(lst[-3: ])

link = 'http://www.main.com/smith/index.html'
print(link[ :4])
print(link[ :4].upper())
print(link.find('smith'))
print(link[20:25])
print(link[20:25].capitalize())
print(link.replace('smith', 'ferreira'))
print(link)
new = link.replace('smith', 'ferreira')
print(new)
print(link.count('/'))
print(link.split('/'))

game = ['Lol', 'D:OS', 'XCOM 2']
for spel in game:
    print(spel)

for spel in game:
    print(spel, end=', ')


weekday = 'wednesday'
month = 'March'
day = 10
year = 2010
hour = 11
minute = 45
second = 33
print(str(hour) + ':' + str(minute) + ':' + str(second))
print('{}:{}:{}'.format(hour, minute, second))
print('{}, {} {} {}, at {}:{}:{}'.format(weekday, month, day, year, hour, minute, second))

for i in range(1,8):
    print(i, i**2, 2**i, i**i)

for i in range(1, 8):
    print('{:1} {:2} {:3} {:6}'.format(i, i**2, 2**i, i**i))

lst = ['Alan Turing', 'Ken Thompson', 'Vint Cerf']
for name in lst:
    f1 = name.split() #de split is gebruikt om de voor en achternaam te splitsen: vervolgens is f1[0] is voornaam
    print(f1[0], f1[1])

for name in lst:
    f1 = name.split()
    print('{:5} {:10}'.format(f1[0], f1[1]))

n = 10
print('{:b}'.format(n))
print('{:c}'.format(n))
print('{:d}'.format(n))
print('{:X}'.format(n))
print('{:e}'.format(n))
print('{:7.2f}'.format(n))

#infile = ('sample.txt') = realtief pad. Dit geeft een foutmelding want niet goede directory
#infline = open('example.txt', 'r')
#infile.close

infile = open('example.txt')
infile.read(1)