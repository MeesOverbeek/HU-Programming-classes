#set1 = {1, 2, 3, 4}
#set2 = {2, 3}

#set1.add(5)
#print(set1)
#set1.remove(5)
#print(set1)
#set1.clear()
#print(set1)
#print(set1.issubset(set2))
#print(set1.issuperset(set2))
#print(set1.union(set2))
#print(set1.intersection(set2))
#print(set1.difference(set2))

import random

def zeeslag(r, c):
    table = (rows*cols-1) * [''] + ['B']
    random.shuffle(table)

    while True:
        pos = input('Enter next position (format: x y): ')
        position = pos.split()
        if table[int(position[0]) * cols + int(position[1])] == 'B':
            print('You found the bomb!')
            break
        else:
            print('No bomb at position', pos)
print(zeeslag(rows, cols))