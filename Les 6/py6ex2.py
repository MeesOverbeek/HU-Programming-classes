input_list = eval(input('Geef een lijst met minimaal 10 strings op: '))
lst = []
if len(input_list) >= 10:
    for item in input_list:
        lst.append(item)
    print(lst)
else:
    print('De lijst is niet 10 strings')


# ["boter", "kaas", "bier", "pizza", "thee", "drop", "koek", "cola", "boterham", "stamppot"]