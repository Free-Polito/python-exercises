#!/usr/bin/env python

# Dichiarazione variabili.
a = 1
somma = 0 

# Gli diciamo come comportarsi.
print ('Inserisci i numeri da aggiungere alla somma ')

# Gli diciamo come terminare.
print ('Quando hai finito inserisci 0')

# Impostiamo un ciclo che quando a e' uguale a 0 termina.
while a != 0 :

        # Gli facciamo visualizzare la somma ogni volta.
        print ("La somma e': ", somma)

        # Con una richiesta di inserimento gli chiediamo quale numero vuole inserire.
        a = float (input('Numero? '))

        # Aggiungiamo a somma,che all'inizio e' 0 sempre il valore di a che inserisce.
        somma = somma + a

# Visualizziamo in fine il totale.
print ('Totale =', somma) 
