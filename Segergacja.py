from Pracownik import Pracownik
from Regal import Regaly
from Towar import Towar


class Segregacja(Pracownik):
    def __init__(self, ID_pracownika):
        super().__init__(ID_pracownika)
        self._stanowisko = "Segregacja"

    def wyswietlPolozenie(self, regal: Regaly):
        regal.pr()

    def nadajPolozenie(self, towar, id, polozenie, regaly: Regaly):
        if isinstance(towar, Towar) and isinstance(id, int) and isinstance(polozenie, int) and id > 0 and polozenie > 0:
            towar.ID_regalu = id
            towar.miejsce = polozenie
            regaly.regal[id][polozenie] = f"id: {towar.ID_produkt}"
        else:
            print("Nieprawidlowy argument!")

    def zwolnijPolozenie(self, towar, id, polozenie, regaly: Regaly):
        if isinstance(towar, Towar) and isinstance(id, int) and isinstance(polozenie, int) and id > 0 and polozenie > 0:
            towar.ID_regalu = None
            towar.miejsce = None
            regaly.regal[id][polozenie] = None
        else:
            print("Nieprawidlowy argument!")

