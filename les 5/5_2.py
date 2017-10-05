with open('kaartnummers.txt', 'r') as naamkaartnummers:
    rows = naamkaartnummers.readlines()
    for row in rows:
        gesplit = row.split(',')
        nummer = gesplit[0]
        naam = gesplit[1].strip()
        print(naam + ' heeft kaartnummer: ' + nummer)

