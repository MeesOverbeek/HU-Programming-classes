cursus = {
    'Bert': 8.2,
    'Piet': 6.6,
    'Klaas': 10.0,
    'Peter': 9.0,
    'Hans': 9.8,
    'Jan': 6.8,
    'Gert': 4.4,
    'Leen': 4.2
}
for name, note in cursus.items():
    if note > 8.9:
        print('{:6}{:6}'.format(name,note))