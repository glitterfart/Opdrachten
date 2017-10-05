def standaardtarief(afstandKM):
    """returns tarief afhankelijk van de kms"""
    if afstandKM <= 50 and afstandKM > 0:
        bedrag = afstandKM * 0.8
    elif afstandKM <= 0:
        bedrag = 0
    else:
        bedrag = 15 + 0.6 * afstandKM
    return bedrag

def ritprijs(leeftijd, weekendrit, afstandKM):
    """returns ritprijs afhankelijk van leeftijd, aftand en of het weekend is."""
    if leeftijd < 12 and leeftijd >= 65:
        if weekendrit is 'ja':
            return standaardtarief(afstandKM)*0.65
        else:
            return standaardtarief(afstandKM)*0.70
    else:
        if weekendrit is 'ja':
            return standaardtarief(afstandKM)*0.60
        else:
            return standaardtarief(afstandKM)*1
for leeftijd in [11, 12, 64, 65]:
    'een for loop om bepaalde waarden te testen'
    for weekendrit in ['ja', 'nee']:
        for afstandKM in range(-10, 81, 40):
            print(round(ritprijs(leeftijd, weekendrit, afstandKM),2))
print('{:6.2f}'.format(23,456789999))