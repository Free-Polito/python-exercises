""" Prendiamo solo alcuni caratteri di una stringa, come una lista di caratteri. """

# Dichiarazione variabili.
py = "Python"
i = 0

# Condizione del ciclo dove i  minore di 6.
while i < 6:
    # Nella prima parte stampiamo lettera per lettera la parola python grazie al
    # contatore i che si incrementa.
    # Dopo la prima tabulazione stampiamo la parola da zero compreso aumentando
    # il contatatore per stampare ad ogni riga tutta la parola python a piccoli
    # passi.Infine con l'ultimo modo uniamo un po i primi due con la differenza
    # che concateniamo le diverse parti.
    print (py[i], '\t', py [0:i + 1], '\t', py[i] + py[i - 1] + py[i - 2])

   # Incrementiamo il contatore.
   i=i+1
