from GestioneFarmacia.GestioneVendite.Prodotto import Prodotto

class Tampone(Prodotto):

    def _init_(self, tipologia, id):
     self.tipologia = tipologia
     self.esito = False
     self.id = id

    def getTipologia(self):
        return self.tipologia

    def setTipologia(self, tipologia):
        self.tipologia = tipologia

    def getId(self):
        return self.id

    def tamponeSvolto(self):
        self.esito = True
        return self.esito

tampone1= Tampone()
tampone1.setCodice('1')
print(tampone1.codice)
