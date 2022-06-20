
def pretty(d, indent=0):
    for key, value in d.items():
        print('\t' * indent + str(key))
        if isinstance(value, dict):
            pretty(value, indent+1)
        else:
            print('\t' * (indent+1) + str(value))


class Regaly():
    def __init__(self, ilosc, miejsca):
        self.regal = {}
        for i in range(1, ilosc + 1):
            self.regal[i] = {}
            for j in range(1, miejsca + 1):
                self.regal[i][j] = None

    def pr(self):
        pretty(self.regal, 0)

