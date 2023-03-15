import pickle
from GestioneFarmacia.GestioneSistema.gestione import Gestore
from GestioneFarmacia.GestioneVendite.Farmaco import Farmaco
from GestioneFarmacia.GestioneVendite.Prodotto import Prodotto

gestore=Gestore()

class GestoreMagazzino:
    def __init__(self):
        self.listaFarmaciMagazzino = []
        self.listaProdottiMagazzino = []
        self.listaProdottiFornitore = []
        self.listaFarmaciFornitore = []



    def downloadMagazzino(self):
        self.downloadFarmaciMagazzino()
        self.downloadProdottiMagazzino()

    def uploadMagazzino(self):
        self.uploadFarmaciMagazzino(self.listaFarmaciMagazzino)
        self.uploadProdottiMagazzino(self.listaProdottiMagazzino)

    def uploadFarmaciFornitore(self):
        f = open(gestore.returnPth()+"GestioneFarmacia/farmaciFornitore", "wb")
        pickle.dump(self.listaFarmaciFornitore, f)

    def uploadProdottiFornitore(self):
        f = open(gestore.returnPth()+"GestioneFarmacia/prodottiFornitore", "wb")
        pickle.dump(self.listaProdottiFornitore, f)

    def uploadFarmaciMagazzino(self):
        f = open(gestore.returnPth()+"GestioneFarmacia/farmaciMagazzino", "wb")
        pickle.dump(self.listaFarmaciMagazzino, f)

    def uploadProdottiMagazzino(self):
        f = open(gestore.returnPth()+"GestioneFarmacia/prodottiMagazzino", "wb")
        pickle.dump(self.listaProdottiMagazzino, f)

    def downloadFarmaciMagazzino(self):
        f = open(gestore.returnPth()+"GestioneFarmacia/farmaciMagazzino", "rb")
        farmaci = pickle.load(f)
        f.close()
        for i in range(len(farmaci)):
            self.listaFarmaciMagazzino.append(farmaci[i])

    def downloadFarmaciFornitore(self):
        f = open(gestore.returnPth()+"GestioneFarmacia/farmaciFornitore", "rb")
        farmaci = pickle.load(f)
        f.close()
        for i in range(len(farmaci)):
            self.listaFarmaciFornitore.append(farmaci[i])

    def downloadProdottiFornitore(self):
        f = open(gestore.returnPth()+"GestioneFarmacia/prodottiFornitore", "rb")
        prodotti = pickle.load(f)
        f.close()
        for i in range(len(prodotti)):
            self.listaProdottiFornitore.append(prodotti[i])

    def downloadProdottiMagazzino(self):
        f = open(gestore.returnPth()+"GestioneFarmacia/prodottiMagazzino", "rb")
        prodotti = pickle.load(f)
        f.close()
        for i in range(len(prodotti)):
            self.listaProdottiMagazzino.append(prodotti[i])

    def showListe(self):
        for i in range(len(self.listaFarmaciMagazzino)):
            print(str(self.listaFarmaciMagazzino[i].codice) + " " +
                  self.listaFarmaciMagazzino[i].nome + " " +
                  self.listaFarmaciMagazzino[i].tipologia + " " +
                  str(self.listaFarmaciMagazzino[i].prezzo) + " " +
                  self.listaFarmaciMagazzino[i].dosaggio + " " +
                  str(self.listaFarmaciMagazzino[i].scadenza) + " " +
                  str(self.listaFarmaciMagazzino[i].giacenza) + " " +
                  str(self.listaFarmaciMagazzino[i].minsan) + " " +
                  str(self.listaFarmaciMagazzino[i].flagRicetta) + " " +
                  str(self.listaFarmaciMagazzino[i].flagBase))
        for i in range(len(self.listaProdottiMagazzino)):
            print(str(self.listaProdottiMagazzino[i].codice) + " " +
                  self.listaProdottiMagazzino[i].nome + " " +
                  self.listaProdottiMagazzino[i].tipologia + " " +
                  str(self.listaProdottiMagazzino[i].prezzo) + " ")
            if((self.listaProdottiMagazzino[i].dosaggio != None)):
                print(self.listaProdottiMagazzino[i].dosaggio + " ")
            if ((self.listaProdottiMagazzino[i].scadenza != None)):
                print(str(self.listaProdottiMagazzino[i].scadenza) + " ")
            print(str(self.listaProdottiMagazzino[i].giacenza) + " ")

f = Farmaco("0000025491734", "Benagol fragola", "Farmaco da banco", 6.70, "16 pastiglie", "2024-09-01", 3, "016242190", False, False)
p = Prodotto("0000092830745", "Allume di potassio", "Prodotti per igiene", 8,"120g",None, 2)
g1 = GestoreMagazzino()
g1.downloadMagazzino()
#g1.listaFarmaciMagazzino.pop(3)
#g1.listaFarmaciMagazzino.append(f)
#g1.listaProdottiMagazzino.append(p)
g1.uploadFarmaciMagazzino()
