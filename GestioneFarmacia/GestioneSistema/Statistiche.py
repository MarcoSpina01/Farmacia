import matplotlib.pyplot as plt

from GestioneFarmacia.GestioneSistema.gestione import Gestore
from GestioneFarmacia.Gui.GestioneTamponi.GraphDialog import GraphDialog
from GestioneFarmacia.GestioneSistema.data import data
# istanza della classe gestore per aquisire il path assoluto
gestore = Gestore()

class Statistiche():

    def __init__(self):
        pass

    # Il metodo plotEsiti crea un pie chart, lo salva come file png e, richiamando setGraph, lo setta come immagine di una label
    def plotPieEsiti(self):
        data.downloadEsiti()
        cp = 0
        cn = 0
        for esiti in data.listaEsiti:
            if esiti.get_tampone().get_esito() == True:
                cp += 1
            else:
                cn += 1

        labels = 'Positivi', 'Negativi'
        sizes = [cp, cn]
        figure, ax = plt.subplots(figsize=(6, 6), dpi=200)
        plt.subplots_adjust(hspace=0)
        ax.pie(sizes, labels=labels,  autopct='%1.1f%%')
        plt.savefig(gestore.returnPth()+ "loghi-icone/esitiplot.png")
        self.g = GraphDialog()
        self.g.setGraph(gestore.returnPth()+ "loghi-icone/esitiplot.png")
