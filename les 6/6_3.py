def seizoen():
    maanden = ['Janurari', 'Februari', 'Maart', 'April', 'Mei', 'Juni', 'Juli', 'Augustus', 'September', 'Oktober', 'November', 'December']
    for maand in maanden:
        zomer = maand[5, 6, 7]
        herfst = maand[8, 9, 10]
        winter = maand[12, 0, 1]
        lente = maand[2, 3, 4]
        user_input= input('noem het getal van de maand:')
        if user_input == [2, 3, 4]:
            print(lente)
        #if input('noem het getal van de maand:') is [5, 6, 7]:
         #   print(zomer)
        #if input('noem het getal van de maand:') is input([8, 9, 10]):
         #   print(winter)
