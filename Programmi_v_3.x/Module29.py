""" Vediamo il comando break. """

# Facciamo inserire un numero dall'utente.
i = int(input("Inserisci un numero: "))

# Mettiamo un ciclo con una condizione i minore di 200.
while i < 200:
    # Una selezione dove se i e' uguale a 0.
    if i == 0:
        #Ferma la selezione.
        break
# Finiamo  con la visulaizzazione del numero.
print ("Il numero e': ", i)

 # E gli diciamo che e' finito il programma.
print ("Finito")
