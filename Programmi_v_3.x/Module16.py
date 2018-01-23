""" Calcoliamo una tavola pitagorica. """

# Titolo.
print (" TAVOLA PITAGORICA\n")

# Variabile contatore.
riga = 1

# Impostazione del ciclo.
while riga <= 10 :

    colonna = 1
    # Impostiamo il secondo ciclo annidato.
    while colonna <= 10 :

        # Stampiamo con una tabulazione il risultato del valore della riga con
        # quello della colonna.
        print ('\t', riga * colonna, end = " ")

        # Incrementiamo il contatore.
        colonna = colonna + 1

    # Incrementiamo l contatore.
    riga = riga + 1
    print("\n")
