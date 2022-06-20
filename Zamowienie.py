from Towar import Towar


class Zamowienie():
    def __init__(self, ID_zamowienie, towary, data, ID_klienta):
        self.ID_zamowienie = ID_zamowienie
        self.__towary = towary
        self.__data = data
        self.stan = "Otwarte"
        self.__ID_klienta = ID_klienta

    # baza danych bedzie to obslugiwala, dla funkcjonowania programu dodane jest to w main
    def dodajZamowienie(self):
        pass

    # tu tak samo
    def usunZamowienie(self):
        pass

    def wyswietlDane(self):
        self.pr()

    def dodajTowar(self, item):
        if isinstance(item, Towar):
            self.__towary.append(item)
        else:
            print("Nieprawidlowy argument!")

    # usun towary
    def usunTowar(self, id):
        if isinstance(id, int):
            for x in self.__towary:
                if x.ID_produkt == id:
                    print("Usunieto produkt o id:", x.ID_produkt)
                    self.__towary.remove(x)
                    self.wyswietlDane()
                    return
        print("Nie znaleziono produktu o id:", id)

    def pr(self):
        print("ID_zamowienia:", self.ID_zamowienie, "ID_klienta:", self.__ID_klienta, "Towary:", *self.__towary, self.__data, self.stan)
