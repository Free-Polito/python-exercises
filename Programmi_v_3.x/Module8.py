#!/usr/bin/env python

numero = 27 #Mettiamo dentro la variabile numero il numero che poi si dovra' indovinare.
indovina = 0 #All'interno di indovina 0.
while indovina!= numero : #Qui definiamo la condizione del ciclo cioe' che indovina diverso da numero.
    indovina = float(input ("Indovina un numero: ")) #Chiediamo all'utente di inserire un numero per provare ad indovinare.
    if indovina > numero: #Per vedere se indovina mettiamo la condizione della selezione.
        print ("Troppo grande") #Se la condizione e' diversa ed e' maggiore.
    elif indovina < numero : #Altrimenti se .
            print ("Troppo piccolo") #La condizione e' diversa ma piu' piccola.

print ("BRAVO!!") #Infine se indovina ci congratuliamo.

