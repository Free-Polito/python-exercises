#!/usr/bin/env python

# Dichiarazione variabili.
i = 1

# Un ciclo con la condizione i minore di 100.
while i < 100 : 
	
	# Facciamo inserire un numero intero all'utente.
	i = int(input('Inserisci un numero: '))

	# Una selezione che ci dice che quando i e' uguale a 0.
	if i == 0: 

		# Ferma la selezione.
	    break 
	
	# Gli stampa mano a mano i numeri che inserisce.
	print ("Il numero e' : ", i) 
	
# Dicimo che il programma e' terminato.
print ('Finito') 

