from Pracownik import Pracownik
from Zamowienie import Zamowienie
from Towar import Towar


class Wysylka(Pracownik):
    def __init__(self, ID_pracownika):
        super().__init__(ID_pracownika)
        self._stanowisko = "Wysylka"

    def zamkniecieProcesu(self, zamowienie):
        if isinstance(zamowienie, Zamowienie):
            if zamowienie.stan == "Zniszczone":
                print("nie mozna wyslac zniszczonego towaru")
            else:
                zamowienie.stan = "Zakonczone"
        else:
            print("Nieprawidlowy argument!")

    def usunTowar(self, towar):
        if isinstance(towar, Towar):
            del towar
        else:
            print("Niepoprawny argument!")