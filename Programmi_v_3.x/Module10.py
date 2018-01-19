#!/usr/bin/env python

i=1 #Inizializziamo la variabile per il ciclo.
n = int(input ("Qual e' il numero di cui vuoi trovare i divisori? ")) #Facciamo inserire un valore numerico all'utente.
print (n, " e' divisibile per ") #Facciamo visualizzare il risultato che ci dara' il ciclo
while i <= n : #Impostiamo il ciclo dove i minore di n
    if n%i == 0 : #Se il numero inserito usando il modulo che ci dara'  il resto della divisione e' uguale a 0.
        print (i) #Se e' vero allora stampa il valore di i.
    i = i + 1 #Incrementiamo in modo da non rendere il ciclo infinito.

