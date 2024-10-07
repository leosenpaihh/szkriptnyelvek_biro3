class Dinoszaurusz:
    def __init__(self, fajta: str, magassag: int):
        self._fajta = fajta
        self._magassag = abs(magassag)
        self._veszelyes = (self._fajta.endswith("rex")
                           or self._magassag > 500)

    @property
    def fajta(self):
        return self._fajta

    @fajta.setter
    def fajta(self, new_fajta: str):
        self._fajta = new_fajta
        self._veszelyes = self._fajta.endswith("rex") or self._magassag > 500

    @property
    def magassag(self):
        return self._magassag

    @magassag.setter        #magassag setter
    def magassag(self, new_magassag: int):
        if new_magassag > 0:
            self._magassag = new_magassag
            self._veszelyes = self._fajta.endswith("rex") or self._magassag > 500

    @property
    def veszelyes(self):
        return self._veszelyes

    @veszelyes.setter
    def veszelyes(self, new_veszelyes: bool):
        if new_veszelyes:
            self._veszelyes = self._fajta.endswith("rex") or self._magassag > 500

    def __iadd__(self, novekedes):
        self._magassag += novekedes
        return self

    def __eq__(self, azonosdinok):
        if not isinstance(azonosdinok, Dinoszaurusz):
            return False
        return (self._fajta == azonosdinok.fajta and
                self._magassag == azonosdinok.magassag and
                self._veszelyes == azonosdinok.veszelyes)