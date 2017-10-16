def lang_genoeg(lengte):
    if lengte >= 120:
        return 'je bent lang genoeg'
    else:
        return 'Sorry, je bent niet lang genoeg'

lengteInvoer = int(input('geef je lengte in centimeter: '))
print(lang_genoeg(lengteInvoer))