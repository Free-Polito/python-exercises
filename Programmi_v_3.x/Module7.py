""" Calcolo dell'area di una figura geometrica con l'aiuto delle funzioni. """

# Funzione che calcola l'area del rettangolo.
def area_rettangolo (base, altezza):
      #La funzione ritorna il risultato.
      return base * altezza

# Funzione che calcola l'area del cerchio, riceve come paramettro il raggio.
def area_cerchio (raggio):
      # Ritorna il risultato dell'operazione.
      return 3.14 * raggio ** 2

# Richiamiamo la funzione area_rettangolo passando come parametri i valori si base e altezza
area_figura = area_rettangolo (3, 2) + area_rettangolo (5, 3) + area_cerchio ( 1/2 )

# Visualizziamo il risultato ottenuto.
print ("L'area della figura e' ", area_figura)
