KAPASITEETTI = 5
OLETUSKASVATUS = 5

class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko

    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.ljono

    def lisaa(self, n):
        if self.kuuluu(n):
            return False
        self.ljono[self.alkioiden_lkm] = n
        self.alkioiden_lkm = self.alkioiden_lkm + 1
        if self.alkioiden_lkm % len(self.ljono) == 0:
            taulukko_old = self.ljono
            self.ljono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
            self.kopioi_lista(taulukko_old, self.ljono)
        return True

    def poista(self, n):
        if self.kuuluu(n):
            self.ljono.remove(n)
            self.alkioiden_lkm -= 1
            return True
        return False

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[0: self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        yhdistetyt = IntJoukko()
        for A in a.to_int_list():
            yhdistetyt.lisaa(A)
        for B in b.to_int_list():
            yhdistetyt.lisaa(B)
        return yhdistetyt

    @staticmethod
    def leikkaus(a, b):
        yhteiset = IntJoukko()
        for A in a.to_int_list():
            if A in b.to_int_list():
                yhteiset.lisaa(A)
        return yhteiset

    @staticmethod
    def erotus(a, b):
        uniikit = IntJoukko()
        for A in a.to_int_list():
            if A not in b.to_int_list():
                uniikit.lisaa(A)
        return uniikit

    def __str__(self):
        return "{" + ", ".join(map(str, self.ljono[0:self.alkioiden_lkm])) + "}"
