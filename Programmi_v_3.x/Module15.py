#!/usr/bin/env python

# Inizializzo la variabile.
i = 1 

# Chiediamo in input di inserire un valore con la virgola di cui si vuole sapere i divisori.
n = float (input ("Quale' il numero di cui vuoi trovare i divisori?")) 

# Visualizziamo il numero dall'utente con una frase.
print (n, "E' divisibile per ") 

#Impostiamo un ciclo che riesegue il blocco di istruzioni finche' i non diventa maggiore o uguale a n.
while i < n :

     #Una condizione con un modulo che ci da il resto della divisione.
    if n % i == 0 :

        #Se e' vero vuol dire che e' divisibile e quindi ne facciamo la stampa.
        print (i) 

    #Incrementiamo i per far finire prima o poi il ciclo.
    i = i + 1 


