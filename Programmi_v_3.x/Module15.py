#!/usr/bin/env python

i=1 #Inizializzo a 1 la variabile contatore.
n = float(input ("Quale' il numero di cui vuoi trovare i divisori?")) #Chiediamo in input di inserire un valore con la virgola di cui si vuole sapere i divisori.

print (n, "E' divisibile per ") #Visualizziamo il numero dall'utente con una frase.

while i < n : #Impostiamo un ciclo che riesegue il blocco di istruzioni finche' i non diventa maggiore o uguale a n.
    if n%i == 0 : #Una condizione con un modulo che ci da il resto della divisione.
        print (i) #Se Ã¨ vero vuol dire che e' divisibile e quindi ne facciamo la stampa.
    i = i + 1 #Incrementiamo i per far finire prima o poi il ciclo.


