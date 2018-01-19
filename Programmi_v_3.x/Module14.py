#!/usr/bin/env python

a = 1 #Variabile contatore impostata a 1.
somma = 0 #Varibile somma contiene 0.
print ('Inserisci i numeri da aggiungere alla somma ') #Gli diciamo come comportarsi.
print ('Quando hai finito inserisci 0') #Gli diciamo come terminare.
while a != 0 : #Impostiamo un ciclo che quando a e' uguale a 0 termina.
        print ("La somma e': ",somma) #Gli facciamo visualizzare la somma ogni volta.
        a = float(input('Numero? ')) #Con una richiesta di inserimento gli chiediamo quale numero vuole inserire.
        somma = somma + a #Aggiungiamo a somma,che all'inizio e' 0 sempre il valore di a che inserisce.
print ('Totale =',somma) #Visualizziamo in fine il totale.
