studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]
def gemiddelde_per_student(studentencijfers):
    lst = []
    for x in studentencijfers:
        lst.append(sum(x)/len(x))
    return lst

def gemiddelde_van_alle_studenten(studentencijfers):
    lst = []
    for x in studentencijfers:
        for s in x:
            lst.append(s)
    gem = sum(lst)/len(lst)
    return gem
print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))