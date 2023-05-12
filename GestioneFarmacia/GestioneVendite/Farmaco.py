from GestioneFarmacia.GestioneVendite.Prodotto import Prodotto

class Farmaco(Prodotto):
    # classe di modellazione

    def __init__(self, codice, nome, tipologia, prezzo, dosaggio, scadenza, giacenza, minsan, flagRicetta, flagBase):
        super().__init__(codice, nome, tipologia, prezzo, dosaggio, scadenza, giacenza)
        self.minsan = minsan
        self.flagRicetta = flagRicetta
        self.flagBase = flagBase
