""" Comando lenght. """

# Dichiariamo e definiamo gli elementi della lista allievi.
allievi = ["Luigi", "Marco", "Filippo", "Paola", "Gabriella", "Silvia"]

# Inizializziamo le variabili
i = 0

# Impostiamo in ciclo dove i deve essere minori della lunghezza della lista allievi usando il comando len.
while i < len (allievi):
	# Andiamo a visualizzare il contenuti di allievi utilizzando il contatore che ad ogni incremento cambia elemento e stampa.
	print (allievi[i], end = " ")
	i = i + 1
