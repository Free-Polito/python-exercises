""" Calcolo del modulo """
# -*- coding: utf-8 -*-

# Inizializziamo le variabili.
i = 1 

# Richiesta input valore numerico.
N = int (input ("Qual e' il numero di cui vuoi trovare i divisori? ")) 

# Visualizzo messaggio. 
print( N, " e' divisibile per: ") 

# Controllo su valore limite. 
while i <= N : 
    
    # Calcolo del modulo 
    if N % i == 0 : 

        # Se il resto è 0 allora stampo 
        print (i) 

    # Incremento contatore.
    i = i + 1 

