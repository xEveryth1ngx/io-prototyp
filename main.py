from Klient import Klient
from Zamowienie import Zamowienie
from Towar import Towar
from Odbior import Odbior
from Segergacja import Segregacja
from Wysylka import Wysylka
from Regal import Regaly


def dodajZamowienie(ID_zamowienie: int, towary: list, data: str, ID_klienta: int):

    for x in towary:
        if not isinstance(x, Towar):
            print("Bledne dane")
            return

    return Zamowienie(ID_zamowienie, towary, data, ID_klienta)


# funkcjonalnosc bedzie obslugiwala baza danych, dodane dla potrzeb prototypu
def usunZamowienie(zamowienia, idx):
    if isinstance(zamowienia[idx], Zamowienie):
        zamowienia.pop(idx)


def przypadek1():
    towary = {}
    zamowienia = list()
    regal = Regaly(2, 5)

    pracownikSegregacja = Segregacja(1)
    pracownikOdbior = Odbior(2)
    pracownikWysylka = Wysylka(3)

    klient = Klient(0, "Jan Nowak", "Szczecin, Niepodległości 34/21", "jan@poczta.pl")

    # pracownik z dzialu "Odbior" dodaje nowe towary
    towary["ksiazka"] = pracownikOdbior.dodajTowar(1, "Harry Potter", 100, "Ksiazka J.K. Rowling")
    towary["plyta"] = pracownikOdbior.dodajTowar(2, "SOAD", 20, "System Of A Down - Toxicity")
    towary["koszulka"] = pracownikOdbior.dodajTowar(3, "T-Shirt Gucci bialy", 200, "T-shirt gucci bawelna 100% bialy")

    # pracownik z dzialu "Segregacja" ustawia towary na regalach i nadaje polozenie
    pracownikSegregacja.nadajPolozenie(towary["ksiazka"], 1, 1, regal)
    pracownikSegregacja.nadajPolozenie(towary["plyta"], 1, 2, regal)
    pracownikSegregacja.nadajPolozenie(towary["koszulka"], 2, 1, regal)
    pracownikSegregacja.wyswietlPolozenie(regal)
    print()

    # zamowienie pobrane z bazy danych
    zamowienia.append(dodajZamowienie(0, [towary["ksiazka"], towary["plyta"], towary["koszulka"]], "29/03/22", 0))

    # pracownik z dzialu "Odbior" otwiera proces zamowienia oraz je skanuje
    pracownikOdbior.skanowanie(zamowienia[0])
    pracownikOdbior.otwarcieProcesu(zamowienia[0])

    # pracownik z dzialu "Segregacja" skanuje zamowienie oraz zmienia jej stan
    pracownikSegregacja.skanowanie(zamowienia[0])
    pracownikSegregacja.zmianaStanu(zamowienia[0], "W trakcie realizacji")

    # pobierane sa produkty potrzebne do zamowienia
    towary["ksiazka"].zmniejszIlosc(1)
    towary["plyta"].zmniejszIlosc(1)
    towary["koszulka"].zmniejszIlosc(1)

    # pracownik z dzialu wysylka skanuje zamowienie oraz zamyka proces przygotowywania paczki
    pracownikWysylka.skanowanie(zamowienia[0])
    pracownikWysylka.zamkniecieProcesu(zamowienia[0])

    zamowienia[0].pr()


def przypadek2():
    towary = {}
    zamowienia = list()
    regal = Regaly(2, 5)

    pracownikSegregacja = Segregacja(1)
    pracownikOdbior = Odbior(2)
    pracownikWysylka = Wysylka(3)

    klient = Klient(0, "Jan Nowak", "Szczecin, Niepodległości 34/21", "jan@poczta.pl")

    # pracownik z dzialu "Odbior" dodaje nowe towary
    towary["ksiazka"] = pracownikOdbior.dodajTowar(1, "Harry Potter", 100, "Ksiazka J.K. Rowling")
    towary["plyta"] = pracownikOdbior.dodajTowar(2, "SOAD", 1, "System Of A Down - Toxicity")
    towary["koszulka"] = pracownikOdbior.dodajTowar(3, "T-Shirt Gucci bialy", 200,
                                                    "T-shirt gucci bawelna 100% bialy")

    # pracownik z dzialu "Segregacja" ustawia towary na regalach i nadaje polozenie
    pracownikSegregacja.nadajPolozenie(towary["ksiazka"], 1, 1, regal)
    pracownikSegregacja.nadajPolozenie(towary["plyta"], 1, 2, regal)
    pracownikSegregacja.nadajPolozenie(towary["koszulka"], 2, 1, regal)
    pracownikSegregacja.wyswietlPolozenie(regal)
    print()

    # zamowienie pobrane z bazy danych
    zamowienia.append(dodajZamowienie(0, [towary["ksiazka"], towary["plyta"], towary["plyta"], towary["koszulka"]], "29/03/22", 0))

    # pracownik z dzialu "Odbior" otwiera proces zamowienia oraz je skanuje
    pracownikOdbior.skanowanie(zamowienia[0])
    pracownikOdbior.otwarcieProcesu(zamowienia[0])

    # pracownik z dzialu "Segregacja" skanuje zamowienie oraz zmienia jej stan
    pracownikSegregacja.skanowanie(zamowienia[0])
    pracownikSegregacja.zmianaStanu(zamowienia[0], "W trakcie realizacji")

    # pobierane sa produkty potrzebne do zamowienia
    towary["ksiazka"].zmniejszIlosc(1)
    # pracownik napotyka problem, na stanie nie znajduje sie dostateczna ilosc produktow
    towary["plyta"].zmniejszIlosc(2)
    # pracownik zmienia status zamowienia na anulowane ze wzgledu na brak wystarczajacej ilosci towaru
    pracownikSegregacja.zmianaStanu(zamowienia[0], "Anulowane")

    # pracownik odkłada wczesniej wziete produkty na miejsce
    towary["ksiazka"].zwiekszIlosc(1)

    zamowienia[0].pr()


def przypadek3():
    towary = {}
    zamowienia = list()
    regal = Regaly(2, 5)

    pracownikSegregacja = Segregacja(1)
    pracownikOdbior = Odbior(2)
    pracownikWysylka = Wysylka(3)

    klient = Klient(0, "Jan Nowak", "Szczecin, Niepodległości 34/21", "jan@poczta.pl")

    towary["ksiazka"] = pracownikOdbior.dodajTowar(1, "Harry Potter", 100, "Ksiazka J.K. Rowling")
    towary["plyta"] = pracownikOdbior.dodajTowar(2, "SOAD", 1, "System Of A Down - Toxicity")
    towary["koszulka"] = pracownikOdbior.dodajTowar(3, "T-Shirt Gucci bialy", 200,
                                                    "T-shirt gucci bawelna 100% bialy")

    pracownikSegregacja.nadajPolozenie(towary["ksiazka"], 1, 1, regal)
    pracownikSegregacja.nadajPolozenie(towary["plyta"], 1, 2, regal)
    pracownikSegregacja.nadajPolozenie(towary["koszulka"], 2, 1, regal)

    zamowienia.append(dodajZamowienie(0, [towary["ksiazka"], towary["plyta"], towary["plyta"], towary["koszulka"]], "29/03/22", 0))

#     Pracownik dostal informacje, ze klient kontaktowal sie z firma, ze przez przypadek zamowil 2 sztuki produktu, prosi o wyslanie jednej
#     2 razy zostala zamowiona plyta, w takim wypadku pracownik usuwa towar o danym id
    zamowienia[0].pr()
    zamowienia[0].usunTowar(2)

#     proces zamowienie przebiega dalej
    pracownikOdbior.skanowanie(zamowienia[0])
    pracownikOdbior.otwarcieProcesu(zamowienia[0])

    pracownikSegregacja.skanowanie(zamowienia[0])
    pracownikSegregacja.zmianaStanu(zamowienia[0], "W trakcie realizacji")

    # pobierane sa produkty potrzebne do zamowienia
    towary["ksiazka"].zmniejszIlosc(1)
    towary["plyta"].zmniejszIlosc(1)
    towary["koszulka"].zmniejszIlosc(1)

#     pracownik zauwaza, ze polka z towarami jest pusta, sprawdza jej stan w systemie
    towary["plyta"].pr()

#     w systemie ilosc produktu wynosi 0, wiec zwalnia w systemie lokalizacje na regale
    pracownikSegregacja.zwolnijPolozenie(towary["plyta"], 1, 2, regal)

    # lokalizacja zostala zwolniona
    regal.pr()

#     proces zamowienia przebiega dalej pomyslnie
    zamowienia[0].pr()


def main():
    przypadek1()
    # przypadek2()
    # przypadek3()


if __name__ == "__main__":
    main()

