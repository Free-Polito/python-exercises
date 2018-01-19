#!/usr/bin/env python

#Dentro la scatola corretto mettiamo la stringa no.
corretto = "no" 

# La condizione del ciclo sara' che corretto uguale a no.
while corretto == "no":

    #Gli chiediamo la risposta al quesito.
    risposta = float (input ("Quanto vale 15 x 17? "))

    # Se la risposta e' corretta all'operazione.
    if risposta == 15 * 17:

        # Dentro la scatola corretto non ci sara' piu' no, ma si.
        corretto = "si"

        # E automaticamente gli facciamo i complimenti.
        print ("Brava!")

    # Altrimenti seconda parte della selezione.
    else: 

        # Corretto rimane uguale a no.
        corretto = "no" 


