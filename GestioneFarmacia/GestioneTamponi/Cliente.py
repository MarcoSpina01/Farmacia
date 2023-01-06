from datetime import datetime

class Cliente:

    def __init__(self, nome, cognome, eta, sesso, dataNascita, telefono, email, luogoNascita, indirizzo, codiceFiscale):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.sesso = sesso
        self.dataNascita = dataNascita
        self.telefono = telefono
        self.email = email
        self.luogoNascita = luogoNascita
        self.indirizzo = indirizzo
        self.codiceFiscale = codiceFiscale

    def compleanno(self):
        if datetime.today() > self.dataNascita:
            self.eta += 1