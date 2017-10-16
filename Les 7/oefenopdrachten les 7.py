

def sum():
    total = int()
    while True:
        nextInt = input('next int: ')
        if nextInt == 'quit' or 'stop':
            break
        total += int(nextInt)
        return total
    print(total)

#def kwadraten_som(grondGetallen):
 #   totaalSom = int()
  #  for getal in grondGetallen:
   #     if getal > 1:
    #        totaalSom += getal**2
    #return totaalSom

#print(kwadraten_som([4, 5, 3, -81]))