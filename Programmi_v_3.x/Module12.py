#!/usr/bin/env python


i = 1 #Inizializziamo la prima variabile contatore(Primo ciclo).
while i <= 10 : #Condizione del ciclo dove i minore o uguale a 10.
    e = 1 #Inizializziamo la seconda variabile contatore(Secondo ciclo annidato).
    while e <= 3 : #Condizione del secondo ciclo dove e deve essere minore o uguale a 3.
        print (i ** e,end=" ") #Adesso stampiamo il valore della variabile i elevato al contenuto della variabile e.
        e = e + 1 #Andiamo ad incrementare la variabile e.
    i = i + 1 #Andiamo ad incrementare la variabile i.

