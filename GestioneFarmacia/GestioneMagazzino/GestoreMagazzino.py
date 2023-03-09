import pickle

from GestioneFarmacia.GestioneVendite.Farmaco import Farmaco
from GestioneFarmacia.GestioneVendite.Prodotto import Prodotto


class GestoreMagazzino:
    def __init__(self):
        self.listaFarmaci = []
        self.listaProdotti = []

    def downloadMagazzino(self):
        self.downloadFarmaciMagazzino()
        self.downloadProdottiMagazzino()

    def downloadFarmaciMagazzino(self):
        f = open("/Users/crowh/PycharmProjects/Farmacia/GestioneFarmacia/farmaci", "rb")
        farmaci = pickle.load(f)
        f.close()
        for i in range(len(farmaci)):
            self.listaFarmaci.append(farmaci[i])


    def downloadProdottiMagazzino(self):
        f = open("/Users/crowh/PycharmProjects/Farmacia/GestioneFarmacia/prodotti", "rb")
        prodotti = pickle.load(f)
        f.close()
        for i in range(len(prodotti)):
            self.listaProdotti.append(prodotti[i])

    def showProdotti(self):
        for i in range(len(self.listaFarmaci)):
            print(str(self.listaFarmaci[i].codice) + " " +
                  self.listaFarmaci[i].nome + " " +
                  self.listaFarmaci[i].tipologia + " " +
                  str(self.listaFarmaci[i].prezzo) + " " +
                  self.listaFarmaci[i].dosaggio + " " +
                  str(self.listaFarmaci[i].scadenza) + " " +
                  str(self.listaFarmaci[i].giacenza) + " " +
                  str(self.listaFarmaci[i].minsan) + " " +
                  str(self.listaFarmaci[i].flagRicetta) + " " +
                  str(self.listaFarmaci[i].flagBase))
        for i in range(len(self.listaProdotti)):
            print(str(self.listaProdotti[i].codice) + " " +
                  self.listaProdotti[i].nome + " " +
                  self.listaProdotti[i].tipologia + " " +
                  str(self.listaProdotti[i].prezzo) + " ")
            if((self.listaProdotti[i].dosaggio != None)):
                print(self.listaProdotti[i].dosaggio + " ")
            if ((self.listaProdotti[i].scadenza != None)):
                print(str(self.listaProdotti[i].scadenza) + " ")
            print(str(self.listaProdotti[i].giacenza) + " ")

#g1 = GestoreMagazzino()
#g1.downloadMagazzino()
#g1.showProdotti()

