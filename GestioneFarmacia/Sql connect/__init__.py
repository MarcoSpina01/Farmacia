import mysql.connector
import GestioneTamponi.Appuntamento

mydb = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='Reflex01mysql',
    port='3306',
    database='python'
)

c1 = mydb.cursor()

c1.execute('SELECT * FROM utente')

users = c1.fetchall()

#Riempi utenti

c1.execute('SELECT * FROM appuntamento')
apps = c1.fetchall()
appuntamenti = []
for i in range(apps.length):
    #Creare oggetto cliente con relativi dati
    #Creare oggetto appuntamento con aggiunta dati cliente
     appuntamenti[i] = appuntamento()
