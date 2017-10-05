nummers = []
namen = []
with open('kaartnummers.txt', 'r') as kaartnummerfile:
    rows = kaartnummerfile.readlines()

    for row in rows:
        gesplit = row.split(',')
        nummers.append(gesplit[0])
        namen.append(gesplit[1])
    grootste = max(nummers)
    index = nummers.index(grootste)
    print('het grootste kaartnummer is:', max(nummers), 'en dat staat op regel', index + 1)

print('deze file telt ' + str(len(rows)) + ' regels')
