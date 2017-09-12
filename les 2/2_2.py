cijferICOR=8
cijferPROG=6
cijferCSN=7
gemmidelde=(cijferICOR+cijferPROG+cijferCSN)/3
beloning= cijferICOR*30+cijferPROG*30+cijferCSN*30

overzicht='Mijn Cijfers (gemmideld een' + str(gemmidelde) + ') leveren een beloning van ' + str(beloning) + ' op!'
print(overzicht)