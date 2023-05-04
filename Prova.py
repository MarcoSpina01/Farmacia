import pickle
from datetime import datetime

from GestioneFarmacia.GestioneSistema.data import gestore
from GestioneFarmacia.GestioneTamponi.ClassiTamponi import Tampone, Cliente, Appuntamento
lista = []

appuntamenti = []
a = 2023
m = 4
g = 18
gg = 17
ggg = 16
datag = datetime(a, m, g)
datagg = datetime(a, m, gg)
dataggg = datetime(a, m, ggg)


nome = "Mario"
n = "Djamel"
nn = "Milan"

cognome = "Balotelli"
c = "Mesbah"
cc = "Skriniar"

cf = "MROBLT"
cff = "DMLMSH"
cfff = "MLNSRN"

eta = 32
e = 38
ee = 28

mail = "mariobalo@gmail.com"
mm = "djamel@hotmail.com"
mmm = "milan@gmail.com"

indirizzo = "Via Turati 3"
ind = "Via Turati 51"
sesso = "Maschio"

tipo = "Molecolare"
ti = "Rapido"

tampone = Tampone(tipo)
tamp = Tampone(ti)
cliente = Cliente(nome, cognome, cf, eta, mail, sesso, indirizzo)
c1 = Cliente(n, c, cff, e, mm, sesso, indirizzo)
c2 = Cliente(nn, cc, cfff, ee, mmm, sesso, ind)

a1 = Appuntamento(cliente, tampone, datag)
a2 = Appuntamento(c1, tampone, datagg)
a3 = Appuntamento(c2, tamp, dataggg)
appuntamenti.append(a1)
appuntamenti.append(a2)
appuntamenti.append(a3)

f = open(gestore.returnPth()+"Farmacia/GestioneFarmacia/appuntamenti.pickle", "wb")
pickle.dump(appuntamenti, f)

f = open(gestore.returnPth() + "GestioneFarmacia/appuntamenti.pickle", "rb")
lista = pickle.load(f)
f.close()
for i in range(len(lista)):
   print( lista[i].get_schedappuntamnto() )