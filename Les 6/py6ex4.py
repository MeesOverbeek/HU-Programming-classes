studentencijfers = [ [95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0] ]
def gemiddelde_per_student(studentencijfers):
    gemiddelde_cijfer_per_student = []
    for Cijfer in studentencijfers:
        gemiddelde_cijfer_per_student.append(sum(Cijfer)/len(Cijfer))
    return gemiddelde_cijfer_per_student

def gemiddelde_van_alle_studenten(studentencijfers):
    gemiddelde_cijfer_alle_studenten = []
    for cijfer in studentencijfers:
        for s in cijfer:
            gemiddelde_cijfer_alle_studenten.append(s)
    gem = sum(gemiddelde_cijfer_alle_studenten)/len(gemiddelde_cijfer_alle_studenten)
    return gem
print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))