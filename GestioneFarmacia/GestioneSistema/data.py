import pickle
from datetime import datetime

from GestioneFarmacia.GestioneSistema.gestione import Gestore
from GestioneFarmacia.GestioneVendite.Farmaco import Farmaco
from GestioneFarmacia.GestioneVendite.Prodotto import Prodotto
from GestioneFarmacia.GestioneMagazzino.Ordine import Ordine

gestore=Gestore()

class data:

    #Inizializziamo le collection di dati(in questo caso liste) per contenere tutti i dati proveniente dai file
    listaAppuntamenti = []
    listaFarmaciMagazzino = []
    listaProdottiMagazzino = []
    listaProdottiFornitore = []
    listaFarmaciFornitore = []
    listaClienti = []
    listaEsiti = []
    archivioOrdini = []
    archivioVendite = []
    nVendite = 0
    nOrdini = 0
    nProdMagaz = 0
    nFarmMagaz = 0
    nProdForn = 0
    nFarmForn = 0

    def __init__(self):
        pass

    today = datetime.now()


    # I metodi di questa classe riguardano esclusivamente la lettura e la scrittura su file di tipo pickle,
    # per quanto riguarda l'upload verrà gestito tramite un semplice dump dei dati presenti a runtime sul programma
    # invece il download viene gestito tramite il metodo load utilizzando una variabile di appoggio.

    @staticmethod
    def uploadArchivioVendite():
        f = open(gestore.returnPth() + "GestioneFarmacia/vendite", "wb")
        pickle.dump(data.archivioVendite, f)
        f.close()

    @staticmethod
    def downloadArchivioVendite():
        f = open(gestore.returnPth() + "GestioneFarmacia/vendite", "rb")
        vendite = pickle.load(f)
        f.close()
        data.archivioVendite.clear()
        for i in range(len(vendite)):
            data.archivioVendite.append(vendite[i])
        data.nVendite = len(data.archivioVendite)

    @staticmethod
    def uploadArchivioOrdini():
        f = open(gestore.returnPth()+"GestioneFarmacia/ordini", "wb")
        pickle.dump(data.archivioOrdini, f)
        f.close()

    @staticmethod
    def downloadArchivioOrdini():
        f = open(gestore.returnPth() + "GestioneFarmacia/ordini", "rb")
        ordini = pickle.load(f)
        f.close()
        data.archivioOrdini.clear()
        for i in range(len(ordini)):
            data.archivioOrdini.append(ordini[i])
        data.nOrdini = len(data.archivioOrdini)

    @staticmethod
    def downloadMagazzino():
        data.downloadFarmaciMagazzino()
        data.downloadProdottiMagazzino()
        data.nProdMagaz = len(data.listaProdottiMagazzino)
        data.nFarmMagaz = len(data.listaFarmaciMagazzino)

    @staticmethod
    def downloadFornitore():
        data.downloadFarmaciFornitore()
        data.downloadProdottiFornitore()
        data.nProdForn = len(data.listaProdottiFornitore)
        data.nFarmForn = len(data.listaFarmaciFornitore)

    @staticmethod
    def uploadFornitore():
        data.uploadFarmaciFornitore()
        data.uploadProdottiFornitore()

    @staticmethod
    def uploadMagazzino():
        data.uploadFarmaciMagazzino()
        data.uploadProdottiMagazzino()

    @staticmethod
    def uploadFarmaciFornitore():
        f = open(gestore.returnPth()+"GestioneFarmacia/farmaciFornitore", "wb")
        pickle.dump(data.listaFarmaciFornitore, f)

    @staticmethod
    def uploadProdottiFornitore():
        f = open(gestore.returnPth()+"GestioneFarmacia/prodottiFornitore", "wb")
        pickle.dump(data.listaProdottiFornitore, f)

    @staticmethod
    def uploadFarmaciMagazzino():
        f = open(gestore.returnPth()+"GestioneFarmacia/farmaciMagazzino", "wb")
        pickle.dump(data.listaFarmaciMagazzino, f)

    @staticmethod
    def uploadProdottiMagazzino():
        f = open(gestore.returnPth()+"GestioneFarmacia/prodottiMagazzino", "wb")
        pickle.dump(data.listaProdottiMagazzino, f)

    @staticmethod
    def uploadAppuntamenti():
        f = open(gestore.returnPth()+"GestioneFarmacia/appuntamenti.pickle", "wb")
        pickle.dump(data.listaAppuntamenti, f)

    @staticmethod
    def downloadFarmaciMagazzino():
        f = open(gestore.returnPth()+"GestioneFarmacia/farmaciMagazzino", "rb")
        farmaci = pickle.load(f)
        f.close()
        data.listaFarmaciMagazzino.clear()
        for i in range(len(farmaci)):
            data.listaFarmaciMagazzino.append(farmaci[i])

    @staticmethod
    def downloadFarmaciFornitore():
        f = open(gestore.returnPth()+"GestioneFarmacia/farmaciFornitore", "rb")
        farmaci = pickle.load(f)
        f.close()
        data.listaFarmaciFornitore.clear()
        for i in range(len(farmaci)):
            data.listaFarmaciFornitore.append(farmaci[i])

    @staticmethod
    def downloadProdottiFornitore():
        f = open(gestore.returnPth()+"GestioneFarmacia/prodottiFornitore", "rb")
        prodotti = pickle.load(f)
        f.close()
        data.listaProdottiFornitore.clear()
        for i in range(len(prodotti)):
            data.listaProdottiFornitore.append(prodotti[i])

    @staticmethod
    def downloadProdottiMagazzino():
        f = open(gestore.returnPth()+"GestioneFarmacia/prodottiMagazzino", "rb")
        prodotti = pickle.load(f)
        f.close()
        data.listaProdottiMagazzino.clear()
        for i in range(len(prodotti)):
            data.listaProdottiMagazzino.append(prodotti[i])

    @staticmethod
    def showMagazzino():
        for i in range(len(data.listaFarmaciMagazzino)):
            print(str(data.listaFarmaciMagazzino[i].codice) + " " +
                  data.listaFarmaciMagazzino[i].nome + " " +
                  data.listaFarmaciMagazzino[i].tipologia + " " +
                  str(data.listaFarmaciMagazzino[i].prezzo) + " " +
                  data.listaFarmaciMagazzino[i].dosaggio + " " +
                  str(data.listaFarmaciMagazzino[i].scadenza) + " " +
                  str(data.listaFarmaciMagazzino[i].giacenza) + " " +
                  str(data.listaFarmaciMagazzino[i].minsan) + " " +
                  str(data.listaFarmaciMagazzino[i].flagRicetta) + " " +
                  str(data.listaFarmaciMagazzino[i].flagBase))
        for i in range(len(data.listaProdottiMagazzino)):
            print(str(data.listaProdottiMagazzino[i].codice) + " " +
                  data.listaProdottiMagazzino[i].nome + " " +
                  data.listaProdottiMagazzino[i].tipologia + " " +
                  str(data.listaProdottiMagazzino[i].prezzo) + " ")
            if((data.listaProdottiMagazzino[i].dosaggio != None)):
                print(data.listaProdottiMagazzino[i].dosaggio + " ")
            if ((data.listaProdottiMagazzino[i].scadenza != None)):
                print(str(data.listaProdottiMagazzino[i].scadenza) + " ")
            print(str(data.listaProdottiMagazzino[i].giacenza) + " ")

    @staticmethod
    def downloadAppuntamenti():
        f = open(gestore.returnPth()+"GestioneFarmacia/appuntamenti.pickle", "rb")
        appuntamenti = pickle.load(f)
        f.close()
        data.listaAppuntamenti.clear()
        for i in range(len(appuntamenti)):
            data.listaAppuntamenti.append(appuntamenti[i])


    @staticmethod
    def downloadClienti():
        data.downloadAppuntamenti()
        temp = []
        for app in data.listaAppuntamenti:
            temp.append(app.get_cliente())
        f = open(gestore.returnPth()+"GestioneFarmacia/archivioclienti.pickle", "wb")
        pickle.dump(temp, f)
        f.close()
        f = open(gestore.returnPth()+"GestioneFarmacia/archivioclienti.pickle", "rb")
        clienti = pickle.load(f)
        f.close()
        data.listaClienti.clear()
        for i in range(len(clienti)):
            data.listaClienti.append(clienti[i])

    @staticmethod
    def downloadEsiti():
        data.downloadAppuntamenti()
        temp = []
        for app in data.listaAppuntamenti:
            if app.get_stato() == True:
                temp.append(app)
        f = open('archivioesiti.pickle', 'wb')
        pickle.dump(temp, f)
        f.close()
        f = open('archivioesiti.pickle', 'rb')
        esiti = pickle.load(f)
        f.close()
        data.listaEsiti.clear()
        for i in range(len(esiti)):
            data.listaEsiti.append(esiti[i])

    @staticmethod
    def uploadEsiti():
        f = open('archivioesiti.pickle', 'wb')
        pickle.dump(data.listaEsiti, f)
    @staticmethod
    def uploadClienti():
        f = open(gestore.returnPth()+"GestioneFarmacia/archivioclienti.pickle", "wb")
        pickle.dump(data.listaClienti, f)