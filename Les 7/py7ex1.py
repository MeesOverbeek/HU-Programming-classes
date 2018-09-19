gegeven_getal = input('Geef een getal: ')
lst=[]
while gegeven_getal != '0':
    lst.append(eval(gegeven_getal))
    gegeven_getal = input('Geef een getal: ')
print('Er zijn ' + str(len(lst)) + ' getallen ingevoerd, de som is ' + str(sum(lst)))