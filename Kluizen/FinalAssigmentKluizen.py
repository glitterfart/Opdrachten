def toon_aantal_kluizen_vrij():
    with open('Kluizen.txt', 'r') as kluizenfile:
        aantaalkluizen = len(kluizenfile.readlines())
        hoeveelkluizenvrij = 12 - aantaalkluizen
        print("het aantal vrije kluizen is", hoeveelkluizenvrij)
    return


def nieuwe_kluis():
    kluisjesfile = open('Kluizen.txt', 'r')
    kluisnummers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    rows = kluisjesfile.readlines()
    for row in rows:
        gesplitst = row.split(';')
        kluisnummer = int(gesplitst[0])
        wactwoord = gesplitst[1]
        kluisnummers.remove(kluisnummer)
    if len(kluisnummers) == 0:
        print('er zijn geen kluisjes meer')
    else:
        print('je krijgt kluisnummer:', kluisnummers[0])
        welkekluisnummer = kluisnummers[0]
        wachtwoord = input("geef een wachtwoord:")
        kluisjesfile.close()

        with open('kluizen.txt', 'a') as kluisjesfile:
            kluisjesfile.write('\n' + str(welkekluisnummer) + ";" + str(wachtwoord))


def kluis_openen():
    kluisjesfile = open('Kluizen.txt', 'r')
    rows = kluisjesfile.readlines()
    kluisnummer = input('wat is je kluis nummer?')
    for row in rows:
        gesplits = row.split(';')


        if int(kluisnummer) == int(gesplits[0]):
            wachtwoord = input('wat is je wachtwoord?')
            if wachtwoord == gesplits[1].strip():
                print('je kluis is geopend')
                return
    print('deze kluis is niet in gebruik')




def close():
    z = 3


def user_input():
    optie1 = '1: Ik wil weten hoeveel kluizen.txt nog vrij zijn'
    optie2 = '2: Ik wil een nieuwe kluis'
    optie3 = '3: Ik wil even iets uit mijn kluis halen'
    optie4 = '4: Exit'
    i = int(input(optie1 + '\n' + optie2 + '\n' + optie3 + '\n' + optie4))

    if i == 1:
        toon_aantal_kluizen_vrij()
    elif i == 2:
        nieuwe_kluis()
    elif i == 3:
        kluis_openen()
    elif i == 4:
        exit


while True:
    user_input()
