user = input('Geef een getal: ')
lst=[]
while user != '0':
    lst.append(eval(user))
    user = input('Geef een getal: ')
print('Er zijn ' + str(len(lst)) + ' getallen ingevoerd, de som is ' + str(sum(lst)))