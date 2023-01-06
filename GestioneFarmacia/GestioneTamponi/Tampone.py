from GestioneFarmacia.GestioneVendite.Prodotto import Prodotto

class Tampone(Prodotto):

    def __init__(self, codice, nome, tipologia, prezzo, dosaggio, scadenza, giacenza):
        super().__init__(codice, nome, tipologia, prezzo, None, scadenza, giacenza)
        self.esito = False


