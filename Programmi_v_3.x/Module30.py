#!/usr/bin/env python


i = 1 #Impostiamo i a 1.
while i < 100 : #Un ciclo con la condizione i minore di 100.
	i = int(input('Inserisci un numero: ')) #Facciamo inserire un numero intero all'utente.
	if i == 0: #Una selezione che ci dice che quando i e' uguale a 0.
	     break #Ferma la selezione.
	print ("Il numero e' : ", i) #Gli stampa mano a mano i numeri che inserisce.
print ('Finito') #Dicimo che il programma e' terminato.

