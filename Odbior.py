from Pracownik import Pracownik
from Zamowienie import Zamowienie
from Towar import Towar


class Odbior(Pracownik):
    def __init__(self, ID_pracownika):
        super().__init__(ID_pracownika)
        self._stanowisko = "Odbior"

    def otwarcieProcesu(self, zamowienie):
        if isinstance(zamowienie, Zamowienie):
            zamowienie.stan = "Przyjete"
        else:
            print("Nieprawidlowy argument!")

    def dodajTowar(self, ID_produkt, nazwa, ilosc, opis):
        return Towar(ID_produkt, nazwa, ilosc, opis)