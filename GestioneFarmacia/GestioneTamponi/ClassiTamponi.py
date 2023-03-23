import datetime

class Cliente:

    def __init__(self, nome, cognome, cf, eta, email, sesso, indirizzo):
        self.nome = nome
        self.cognome = cognome
        self.cf = cf
        self.eta = eta
        self.email = email
        self.sesso = sesso
        self.indirizzo = indirizzo

    def get_nome(self):
        return self.nome

    def get_cognome(self):
        return self.cognome

    def get_cf(self):
        return self.cf

    def get_eta(self):
        return self.eta

    def get_email(self):
        return self.email

    def get_sesso(self):
        return self.sesso

    def get_indirizzo(self):
        return self.indirizzo

    def get_schedacliente(self):
        return f"Dati Cliente\n Nome:{self.nome} Cognome:{self.cognome} Cf:{self.cf} "


class Tampone():
    def __init__(self, tipo):
        self.codicetampone = "00000529459202"
        self.tipo = tipo
        if self.tipo == "Molecolare":
            self.prezzo = 50
        elif self.tipo == "Rapido":
            self.prezzo = 5
        self.esito = False

    def get_tipo(self):
        return self.tipo
    def get_prezzo(self):
        return self.prezzo
    def set_tipo(self, tipo):
        self.tipo = tipo

    def get_esito(self):
        return self.esito

    def get_codtampone(self):
        return self.codicetampone

    def set_esito(self):
        self.esito = True

    def get_schedatampone(self):
        return f"Dati Tampone\n Nome:{self.get_tipo()} Cognome:{self.get_esito()} Cf:{self.get_prezzo()} "


class Appuntamento:
    #counter = 0

    def __init__(self, cliente: Cliente, tampone: Tampone, data: datetime):
        self.cliente = cliente
        #self.id_app = Appuntamento.counter
       # Appuntamento.counter += 1
        self.esito = False
        self.data = data
        self.isconcluso = False
        self.tampone = tampone

    def set_isconcluso(self):
        self.isconclusa = True

    def get_esito(self):
        return self.esito

    def set_idapp(self, n: int):
        self.id_app = n

    def get_tampone(self):
        return self.tampone

    def get_idapp(self):
        return self.id_app

    def get_stato(self):
        return self.isconcluso

    def get_cliente(self):
        return self.cliente

    def get_data(self):
        return self.data

    def get_cff(self):
        return self.get_cliente().get_cf()

    def get_schedappuntamnto(self):
        return f"Codice Appuntamento:{self.get_idapp()} cf:{self.get_cliente().get_cf()} Data:{self.data}"
