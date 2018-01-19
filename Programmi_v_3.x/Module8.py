#!/usr/bin/env python

# Dichiariamo le variabili.
# Dentro la variabile ci sara' il numero che bisognera' indovinare.
numero = 27  
indovina = 0 

# Qui definiamo un ciclo dove impostiamo indovina diverso da numero.
while indovina != numero :

    # Chiediamo all'utente di inserire un numero per provare ad indovinare.
    indovina = float (input ("Indovina un numero: ")) 

    # Per vedere se ha indovinato mettiamo un controllo
    if indovina > numero: 
        # Se il numero e' troppo grande.
        print ("Troppo grande") 
    
    elif indovina < numero:
        # Se il numero è piu' piccolo.
        print ("Troppo piccolo") 

#Infine se indovina ci congratuliamo.
print ("BRAVO!!") 

