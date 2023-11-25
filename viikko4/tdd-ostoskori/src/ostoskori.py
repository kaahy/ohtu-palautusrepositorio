from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self._ostokset = []

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 
        lkm = 0
        for ostos in self._ostokset:
            lkm += ostos.lukumaara()
        return lkm

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        hinta = 0
        for ostos in self._ostokset:
            hinta += ostos.hinta()
        return hinta

    def lisaa_tuote(self, lisattava: Tuote):
        found = False
        for ostos in self._ostokset:
            if lisattava.nimi == ostos.tuotteen_nimi:
                ostos.lukumaara += 1
                found = True
                break

        if not found:
            self._ostokset.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        return self._ostokset