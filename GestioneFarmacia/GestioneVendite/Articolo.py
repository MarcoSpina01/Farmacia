from GestioneFarmacia.GestioneVendite.Prodotto import Prodotto

class Articolo(Prodotto):

    def _init_(self, nome, quantita, descrizione, prezzo, scadenza):
     self.nome = nome
     self.quantita = quantita
     self.descrizione = descrizione
     self.prezzo = prezzo
     self.scadenza = scadenza

