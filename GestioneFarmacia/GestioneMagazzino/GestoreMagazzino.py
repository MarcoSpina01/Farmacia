import pickle

from GestioneFarmacia.GestioneVendite.Farmaco import Farmaco


class GestoreMagazzino:
    def __init__(self):
        self.listaProdotti = []


    def downloadMagazzino(self):
        f = open("farmaci", "rb")
        data = pickle.load(f)
        f.close()
        for i in range(len(data)):
            self.listaProdotti.append(data[i])

    def showProdotti(self):
        for i in range(len(self.listaProdotti)):
            print(str(self.listaProdotti[i].codice) + " " +
                  self.listaProdotti[i].nome + " " +
                  self.listaProdotti[i].tipologia + " " +
                  str(self.listaProdotti[i].prezzo) + " " +
                  self.listaProdotti[i].dosaggio + " " +
                  str(self.listaProdotti[i].scadenza) + " " +
                  str(self.listaProdotti[i].giacenza) + " " +
                  str(self.listaProdotti[i].minsan) + " " +
                  str(self.listaProdotti[i].flagRicetta) + " " +
                  str(self.listaProdotti[i].flagBase))


g1 = GestoreMagazzino()
g1.downloadMagazzino()
g1.showProdotti()

