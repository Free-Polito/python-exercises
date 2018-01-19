#!/usr/bin/env python

# Inizializziamo la prima variabile contatore(Primo ciclo).
i = 1

# Condizione del ciclo dove i minore o uguale a 10.
while i <= 10 :
    
    # Inizializziamo la seconda variabile contatore(Secondo ciclo annidato).
    e = 1 

    # Condizione del secondo ciclo dove e deve essere minore o uguale a 3.
    while e <= 3 :

        # Adesso stampiamo il valore della variabile i elevato al contenuto della variabile e.
        print (i ** e, end = " ")

        # Andiamo ad incrementare la variabile e.
        e = e + 1 

    # Andiamo ad incrementare la variabile i.
    i = i + 1 

