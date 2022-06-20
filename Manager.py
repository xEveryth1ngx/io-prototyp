from Pracownik import Pracownik


class Manager(Pracownik):
    def __init__(self, ID_pracownika, stanowisko):
        self._stanowisko = "Menedżer"

    # funkcjonalnosc z bazy danych
    def generowanieRaportu(self):
        pass

    # tak samo jak z poprzednim
    def przejrzyjBaze(self):
        pass