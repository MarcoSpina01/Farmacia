class Appuntamento:

    def _init_(self, data , cliente, tampone, ora):
        self.data = data
        self.id = 1  #Da implementare
        self.cliente = cliente
        self.tampone = tampone
        self.ora = ora

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getId(self):
        return self.id

    def setCliente(self, cliente):
        self.cliente = cliente

    def getCliente(self):
        return self.cliente

    def getTampone(self):
        return self.tampone

    def setTampone(self, tampone):
        self.tampone = tampone

    def getOra(self):
        return self.ora

    def setOra(self, ora):
        self.ora = ora