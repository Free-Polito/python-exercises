""" Calcolo del modulo """
# -*- coding: utf-8 -*-

#Inizializziamo la variabile per il ciclo.
i = 1 
#Facciamo inserire un valore numerico all'utente.
N = int (input ("Qual e' il numero di cui vuoi trovare i divisori? ")) 
#Facciamo visualizzare il risultato che ci dara' il ciclo
print( N, " e' divisibile per: ") 
#Impostiamo il ciclo dove i minore di n
while i <= N : 
    # Se il numero inserito usando il modulo che ci dara'  il resto della
    # divisione e' uguale a 0.
    if N % i == 0 : 
        #Se e' vero allora stampa il valore di i.
        print (i) 
    #Incrementiamo in modo da non rendere il ciclo infinito.
    i = i + 1 

