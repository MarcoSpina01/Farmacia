from GestioneFarmacia.GestioneVendite.Prodotto import Prodotto

class Farmaco(Prodotto):

    def _init_(self, farmacode, dosaggio, ricetta, unitaMisuraDosaggio):
     self.farmacode = farmacode
     self.dosaggio = dosaggio
     self.ricetta  = False
     self.unitaMisuraDosaggio = unitaMisuraDosaggio

farmaco1=Farmaco()
farmaco1.setCodice('1')
print(farmaco1.codice)
