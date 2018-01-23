""" Uso di funzioni per la verifica della correttezza delle risposte alle
domande. """

# Andiamo a definire una funzione che richiameremo, per non scrivere ogni volta
# lo stesso codice.
def interrogazione (domanda, risposta_esatta):
	# Andiamo a scrivere la prima domanda.
	risposta_allievo = input (domanda)

	# Con una condizione controlliamo se la risposta data e' uguale a quella esatta.
	if risposta_esatta == risposta_allievo:
	  # Gli diciamo che e' giusto, facendo anche dei complimenti.
	  print ("La risposta e' esatta")
	  print ("Bravissimo")
	# Altrimenti diciamo che e' sbagliata, dando la soluzione e un consiglio.
	else:
	  print ("Risposta errata")
	  print ("La risposta esatta e' ", risposta_esatta, ".")
	  print (" Studia di piu'!")

# Variabile che contiene la domanda.
domanda1 = "In che anno e' caduto l'impero romano d'occidente? "
# Risposta corretta alla domanda.
risposta_esatta1 = "476"
# Richiamiamo la funzione interrogazione.
interrogazione (domanda1, risposta_esatta1)

domanda2 = "Chi e' stato il primo presidente degli Stati Uniti? "
risposta_esatta2 = "Washington"
interrogazione (domanda2, risposta_esatta2)

domanda3 = "In che anno e' terminata la prima guerra mondiale? "
risposta_esatta3 = "1918"
interrogazione (domanda3, risposta_esatta3)
