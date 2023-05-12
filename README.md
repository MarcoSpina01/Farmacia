# *GESTIONE FARMACIA*


[![N|Solid](https://www.boomerangcard.it/it/uploads/esercente/54/logo.png)](https://nodesource.com/products/nsolid)


Il progetto si propone di modellare un sistema informatico per la gestione di una farmacia.
L’ipotesi di modellazione alla quale il progetto aderirà sarà quella di una farmacia rurale, il cui personale è composto unicamente dal Direttore Responsabile, addetto alla vendita di farmaci e all’esecuzione di tamponi. 

Il sistema garantirà all’Amministratore l’accesso a funzionalità che consentono la gestione di una serie di operazioni quali:
- Registrazione delle vendite al banco
- Gestione magazzino ( compresa la creazione di ordini verso il fornitore)
- Gestione degli archivi
- Gestione dell'area tamponi (prenotazione ed effettuazione )

## Installation

Il software è stato sviluppato in Python con l'ausilio di PyCharm. 

[![Build Status](https://i.stack.imgur.com/wJqaA.png)](https://travis-ci.org/joemccann/dillinger)


Per installare installare il progetto su PyCharm:
- Dal menu principale, scegli Git | Clone. Se il menu Git non è disponibile, scegli VCS | Ottieni da Controllo versione.
- Nella finestra di dialogo Ottieni da controllo versione, scegli GitHub a sinistra.
- Accedi a GitHub effettuando una delle seguenti operazioni:
- Se disponi di un token, fai clic su Usa token, quindi incolla il token nel campo Token e fai clic su Accedi.
- Altrimenti, fai clic su Accedi tramite GitHub.
- Inserisci le tue credenziali GitHub nella finestra del browser che si apre. Se hai abilitato l'autenticazione a due fattori, ti verrà chiesto di inserire un codice che ti verrà inviato tramite SMS o tramite l'applicazione mobile.
- Seleziona la repository da GitHub associati 
- Nel campo Directory, inserisci il percorso della cartella in cui verrà creato il tuo repository Git locale.
- Fare clic su Clona.


# FEATURES
## Gestione Farmacia -  LOGIN
[![Build Status](inserire link foto login una volta aggiunta la cartella)]
La schermata di Login consente all'Amministratore di accedere al menù. In caso di problematiche è garantita la possibilità di contattare l'assistenza.
## Gestione Farmacia - FUNZIONALITA'
In seguito al login si accede al menu delle funzionalità attraverso il quale è possibile selezionare a quale schermata accedere e quali operazioni effettuare. 
## Gestione Farmacia - TAMPONI
[![Build Status](inserire link foto tamponi una volta aggiunta la cartella)]

La Gestione Tamponi consente:
- Visualizzare gli appuntamenti: cliccando sulla data dell'appuntamento sul calendario nella tabella compariranno le relative informazioni. In alternativa è possibile filtrare tramite *Ricerca per* ottenendo o solo gli appuntamenti *conclusi* (ossia con esito) o solo quelli *non conclusi* (ossia senza esito)
- Aggiungere un nuovo appuntamento: cliccando *Nuovo Appuntamento* si aprirà un modulo da compilare attraverso il quale, dopo aver premuto *Registrati*, l'appuntamento verrà creato e aggiunto al calendario
- Eliminare un appuntamento: selezionando l'appuntamento è possbile procedere alla sua eliminazione
