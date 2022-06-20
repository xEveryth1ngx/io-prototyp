

class Towar():
    def __init__(self, ID_produkt, nazwa, ilosc, opis):
        self.ID_produkt = ID_produkt
        self.__ilosc = ilosc
        self.__opis = opis
        self.__nazwa = nazwa
        self.ID_regalu = None
        self.miejsce = None

    def zmniejszIlosc(self, sztuki):
        if isinstance(sztuki, int) and sztuki > 0:
            if self.__ilosc - sztuki >= 0:
                self.__ilosc -= sztuki
                return 1
            else:
                print("Niepoprawna ilosc")
                return 0
        else:
            print("Nieprawidlowy argument!")

    def zwiekszIlosc(self, sztuki):
        if isinstance(sztuki, int) and sztuki > 0:
            self.__ilosc += sztuki
        else:
            print("Nieprawidlowy argument!")

    def wadliwyTowar(self):
        print("Zgloszono wadliwy towar")
        self.zmniejszIlosc(1)

    def pr(self):
        print(self.ID_produkt, self.__nazwa, self.__ilosc, self.__opis)

    def __str__(self):
        return f"{self.ID_produkt}:{self.__nazwa} "