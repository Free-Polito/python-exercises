#!/usr/bin/env python

print (" TAVOLA PITAGORICA\n") #Titolo.
riga = 1 #Variabile contatore.
while riga <= 10 : #Impostazione del ciclo.
    colonna = 1
    while colonna <= 10 : #Impostiamo il secondo ciclo.
        print ('\t', riga * colonna, end=" ")
        colonna = colonna + 1#Incrementiamo il contatore.
    riga = riga + 1 #Incrementiamo l contatore.
    print("\n")

