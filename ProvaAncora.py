import pickle

from GestioneFarmacia.Gui.GestioneArchivio.archivio import gestore


clienti = []
f = open(gestore.returnPth() + "Farmacia/GestioneFarmacia/appuntamenti.pickle", "rb")
lista = pickle.load(f)
f.close()

for app in lista:
    persona = app.get_cliente()
    clienti.append(persona)

f = open(gestore.returnPth()+"Farmacia/GestioneFarmacia/archivioclienti.pickle", "wb")
pickle.dump(clienti, f)
print("fatto")

