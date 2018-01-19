#!/usr/bin/env python

corretto = "no" #Dentro la scatola corretto mettiamo la stringa no.
while corretto == "no": #La condizione del ciclo sara' che corretto uguale a no.
    risposta = float(input ("Quanto vale 15 x 17? ")) #Gli chiediamo la risposta al quesito.
    if risposta == 15*17:#Se la risposta e' corretta all'operazione.
        corretto = "si" #Dentro la scatola corretto non ci sara' piu' no, ma si.
        print ("Brava!") #E automaticamente gli facciamo i complimenti.
    else: #Altrimenti seconda parte della selezione.
        corretto = "no" #Corretto rimane uguale a no.


