from enum import Enum
from tkinter import ttk, constants, StringVar

class Summa:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.io = sovelluslogiikka
        self.lue_syote = lue_syote

    def suorita(self):
        luku = int(self.lue_syote())
        muisti.paivita(luku)
        self.io.plus(luku)

class Erotus:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.io = sovelluslogiikka
        self.lue_syote = lue_syote

    def suorita(self):
        luku = int(self.lue_syote())
        muisti.paivita(-luku)
        self.io.miinus(luku)

class Nollaus:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.io = sovelluslogiikka
        self.lue_syote = lue_syote

    def suorita(self):
        self.io.nollaa()

class Kumoa:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.io = sovelluslogiikka
        self.lue_syote = lue_syote

    def suorita(self):
        arvo = self.io.arvo()
        lisattava = muisti.hae_muistista() * -1
        self.io.aseta_arvo(arvo + lisattava)

class Muisti:
    def __init__(self):
        self._muutokset = [0]

    def paivita(self, muutos=0):
        self._muutokset.append(muutos)

    def _poista_viimeinen(self):
        self._muutokset.pop()
        if len(self._muutokset) == 0:
            self._muutokset = [0]

    def hae_muistista(self):
        uusin_muutos = self._muutokset[-1]
        self._poista_viimeinen()
        return uusin_muutos

class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4

class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root

        self._komennot = {
            Komento.SUMMA: Summa(sovelluslogiikka, self._lue_syote),
            Komento.EROTUS: Erotus(sovelluslogiikka, self._lue_syote),
            Komento.NOLLAUS: Nollaus(sovelluslogiikka, self._lue_syote),
            Komento.KUMOA: Kumoa(sovelluslogiikka, self._lue_syote)
        }

    def kaynnista(self):
        global muisti
        muisti = Muisti()
        self._arvo_var = StringVar()
        self._arvo_var.set(self._sovelluslogiikka.arvo())
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._arvo_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _lue_syote(self):
        return self._syote_kentta.get()

    def _suorita_komento(self, komento):
        komento_olio = self._komennot[komento]
        komento_olio.suorita()
        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovelluslogiikka.arvo() == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._arvo_var.set(self._sovelluslogiikka.arvo())
