#!/usr/bin/env python
def area_rettangolo (base, altezza): #Funzione che va a calcolare l'area del rettangolo.
      return base * altezza
def area_cerchio (raggio): #Funzione che va a calcolare l'area del cerchio.
      return 3.14 * raggio**2
area_figura = area_rettangolo (3,2)+area_rettangolo (5,3)+area_cerchio(1/2) #Andiamo a richiamare le funzione e a ffare le operazioni trovando l'aera totale.
print("L'area della figura e' ",area_figura) #Visualizziamo infine il risultato ottenuto.



