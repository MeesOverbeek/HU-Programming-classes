def ticker(filename):
    content = open(filename, 'r')
    reader = content.readlines()
    ijlst = []
    for x in reader:
        ijlst.append(x.strip().split(':'))
    dic = {}
    for x in ijlst:
        key = x[0]
        value = x[1]
        dic[key] = value
    print(dic)

    lst2 = []
    for x in dic.values():
        lst2.append(x)
    company = input('Voer een bedrijfsnaam in: ')
    if company in dic:
        print(dic[company])
    elif company not in dic:
        for x,y  in dic.items():
            if y == company:
                print(x)
ticker('ticker.txt')