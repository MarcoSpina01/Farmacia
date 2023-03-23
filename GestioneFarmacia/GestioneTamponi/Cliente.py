from datetime import datetime

class Cliente:

    def __init__(self, nome, cognome, eta, sesso, email, indirizzo, codiceFiscale):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.sesso = sesso
        self.email = email
        self.indirizzo = indirizzo
        self.codiceFiscale = codiceFiscale

