from Zamowienie import Zamowienie


class Pracownik():
    def __init__(self, ID_pracownika):
        self.ID_pracownika = ID_pracownika

    def skanowanie(self, zamowienie):
        if isinstance(zamowienie, Zamowienie):
            zamowienie.pr()
        else:
            print("Nieprawidlowy argument!")

    def zmianaStanu(self, zamowienie, nowyStan):
        if isinstance(zamowienie, Zamowienie):
            mozliwosci = ("Zapłacone", "Anulowane", "W trakcie realizacji", "Zakonczone", "Przyjete", "Zniszczone")
            if nowyStan in mozliwosci:
                zamowienie.stan = nowyStan
            else:
                print("Bledny stan")
        else:
            print("Nieprawidlowy argument!")

