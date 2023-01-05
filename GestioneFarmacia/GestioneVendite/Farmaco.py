from GestioneFarmacia.GestioneVendite.Prodotto import Prodotto

class Farmaco(Prodotto):

    def __init__(self,codice, nome, tipologia, prezzo, dosaggio, scadenza, giacenza, minsan, flagRicetta):
        super().__init__(codice, nome, tipologia, prezzo, dosaggio, scadenza, giacenza)
        self.minsan = minsan
        self.flagRicetta = flagRicetta




